
import json
import boto3
from decimal import Decimal
from botocore.exceptions import ClientError

# Connect to DynamoDB
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Employees")


# Convert Decimal into JSON-compatible numbers
def decimal_converter(obj):
    if isinstance(obj, Decimal):
        if obj % 1 == 0:
            return int(obj)
        return float(obj)

    raise TypeError("Object is not JSON serializable")


# Common API response
def response(status_code, data):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(data, default=decimal_converter)
    }


# Main Lambda handler
def lambda_handler(event, context):

    print("Employee API started")
    print("Received event:", json.dumps(event))

    try:
        # Get HTTP method
        method = event["requestContext"]["http"]["method"]

        # Get request path
        path = event["rawPath"]

        # Remove API stage prefix, such as /dev
        stage = event["requestContext"]["stage"]

        if stage != "$default":
            prefix = "/" + stage
            if path == prefix:
                path = "/"
            elif path.startswith(prefix + "/"):
                path = path[len(prefix):]

        # Get employee ID
        path_parameters = event.get("pathParameters") or {}
        employee_id = path_parameters.get("employeeId")

        print("Method:", method)
        print("Normalized path:", path)
        print("Employee ID:", employee_id)

        # CREATE EMPLOYEE
        if method == "POST" and path == "/employees":

            body = json.loads(event.get("body") or "{}")

            required_fields = [
                "employeeId", "name", "department", "salary"
            ]

            for field in required_fields:
                if field not in body:
                    return response(400, {
                        "message": f"Missing required field: {field}"
                    })

            if not isinstance(body["employeeId"], str) or not body["employeeId"].strip():
                return response(400, {"message": "Invalid employeeId"})

            if not isinstance(body["name"], str) or not body["name"].strip():
                return response(400, {"message": "Invalid name"})

            if not isinstance(body["department"], str) or not body["department"].strip():
                return response(400, {"message": "Invalid department"})

            if isinstance(body["salary"], bool) or not isinstance(body["salary"], (int, float)):
                return response(400, {"message": "Salary must be a number"})

            if body["salary"] < 0:
                return response(400, {"message": "Salary cannot be negative"})

            employee = {
                "employeeId": body["employeeId"].strip(),
                "name": body["name"].strip(),
                "department": body["department"].strip(),
                "salary": Decimal(str(body["salary"]))
            }

            table.put_item(
                Item=employee,
                ConditionExpression="attribute_not_exists(employeeId)"
            )

            return response(201, {
                "message": "Employee added successfully",
                "employee": employee
            })

        # GET ALL EMPLOYEES
        elif method == "GET" and path == "/employees":

            result = table.scan()
            employees = result.get("Items", [])

            return response(200, {
                "message": "Employees retrieved successfully",
                "totalEmployees": len(employees),
                "employees": employees
            })

        # GET ONE EMPLOYEE
        elif method == "GET" and employee_id:

            result = table.get_item(
                Key={"employeeId": employee_id}
            )

            employee = result.get("Item")

            if not employee:
                return response(404, {
                    "message": "Employee not found"
                })

            return response(200, {
                "message": "Employee found successfully",
                "employee": employee
            })

        # UPDATE EMPLOYEE
        elif method == "PUT" and employee_id:

            body = json.loads(event.get("body") or "{}")

            allowed_fields = {"name", "department", "salary"}

            if not body:
                return response(400, {
                    "message": "Provide at least one field to update"
                })

            if not all(field in allowed_fields for field in body):
                return response(400, {
                    "message": "Only name, department and salary can be updated"
                })

            for field in ("name", "department"):
                if field in body and (
                    not isinstance(body[field], str) or not body[field].strip()
                ):
                    return response(400, {
                        "message": f"{field} must be a non-empty string"
                    })

            if "salary" in body:
                if isinstance(body["salary"], bool) or not isinstance(body["salary"], (int, float)):
                    return response(400, {"message": "Salary must be a number"})

                if body["salary"] < 0:
                    return response(400, {"message": "Salary cannot be negative"})

            update_parts = []
            expression_values = {}

            for field, value in body.items():
                placeholder = ":" + field
                update_parts.append(f"{field} = {placeholder}")

                if field == "salary":
                    expression_values[placeholder] = Decimal(str(value))
                else:
                    expression_values[placeholder] = value.strip()

            result = table.update_item(
                Key={"employeeId": employee_id},
                UpdateExpression="SET " + ", ".join(update_parts),
                ExpressionAttributeValues=expression_values,
                ConditionExpression="attribute_exists(employeeId)",
                ReturnValues="ALL_NEW"
            )

            return response(200, {
                "message": "Employee updated successfully",
                "employee": result.get("Attributes")
            })

        # DELETE EMPLOYEE
        elif method == "DELETE" and employee_id:

            result = table.delete_item(
                Key={"employeeId": employee_id},
                ConditionExpression="attribute_exists(employeeId)",
                ReturnValues="ALL_OLD"
            )

            return response(200, {
                "message": "Employee deleted successfully",
                "employee": result.get("Attributes")
            })

        # INVALID ROUTE
        else:
            return response(404, {
                "message": "Route not found"
            })

    except ClientError as e:

        error_code = e.response["Error"]["Code"]
        print("AWS Error:", str(e))

        if error_code == "ConditionalCheckFailedException":
            return response(409, {
                "message": "Employee already exists or does not exist"
            })

        return response(500, {
            "message": "DynamoDB operation failed",
            "error": str(e)
        })

    except (json.JSONDecodeError, TypeError, ValueError) as e:

        return response(400, {
            "message": "Invalid request data",
            "error": str(e)
        })

    except Exception as e:

        print("Unexpected Error:", str(e))

        return response(500, {
            "message": "Internal server error",
            "error": str(e)
        })
