
# AWS API Gateway Employee Management System

## Project Overview

This project demonstrates how to build a serverless Employee Management API using Amazon Web Services (AWS).

The application allows users to create, retrieve, update, and delete employee records through REST API endpoints.

The backend is developed using Python and AWS Lambda, while Amazon DynamoDB is used to store employee information.

## AWS Services Used

- Amazon API Gateway (HTTP API)
- AWS Lambda
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch

## Architecture

```text
             Client / Postman
                    |
                    v
             API Gateway
                    |
                    v
             AWS Lambda
              (Python)
                    |
                    v
              DynamoDB
             (Employees)
                    |
                    v
             Store Employee
                Records
```

CloudWatch is used to monitor Lambda execution and application logs.

## Technology Stack

| Technology | Purpose |
|---|---|
| AWS | Cloud Infrastructure |
| Python | Backend Programming |
| Boto3 | AWS SDK for Python |
| API Gateway | API Management |
| Lambda | Serverless Computing |
| DynamoDB | NoSQL Database |
| Postman | API Testing |

## DynamoDB Configuration

**Table Name:** Employees

**Partition Key:** employeeId

**Partition Key Type:** String

Example employee record:

```json
{
    "employeeId": "101",
    "name": "Rahul",
    "email": "rahul@example.com",
    "department": "IT",
    "age": 25
}
```

## API Endpoints

The application supports the following CRUD operations.

| HTTP Method | Endpoint | Description |
|---|---|---|
| POST | /employees | Create a new employee |
| GET | /employees | Retrieve all employees |
| GET | /employees/{id} | Retrieve employee by ID |
| PUT | /employees/{id} | Update employee details |
| DELETE | /employees/{id} | Delete an employee |

### 1. Create Employee

**Method:** POST

**Endpoint:**
```text
/employees
```

**Request Body:**

```json
{
    "employeeId": "101",
    "name": "Rahul",
    "email": "rahul@example.com",
    "department": "IT",
    "age": 25
}
```

### 2. Get All Employees

**Method:** GET

**Endpoint:**
```text
/employees
```

Returns employee records stored in DynamoDB.

### 3. Get Employee by ID

**Method:** GET

**Endpoint:**
```text
/employees/101
```

Retrieves employee information using the employee ID.

### 4. Update Employee

**Method:** PUT

**Endpoint:**
```text
/employees/101
```

**Request Body:**

```json
{
    "name": "Rahul Sharma",
    "email": "rahul.sharma@example.com",
    "department": "Cloud Engineering",
    "age": 26
}
```

Updates the specified employee record.

### 5. Delete Employee

**Method:** DELETE

**Endpoint:**
```text
/employees/101
```

Deletes the employee record from DynamoDB.

## Lambda Function

The AWS Lambda function is developed using Python.

It uses Boto3 to interact with the DynamoDB Employees table.

Main responsibilities:

- Process API Gateway requests.
- Read employee information.
- Create employee records.
- Update employee information.
- Delete employee records.
- Convert DynamoDB Decimal values into JSON-compatible numbers.
- Return HTTP responses in JSON format.
- Handle application errors.

## IAM Permissions

An IAM execution role is attached to the Lambda function.

The role provides the necessary permissions to access the DynamoDB Employees table.

This allows Lambda to interact with DynamoDB without storing AWS access keys in the code.

## CloudWatch Monitoring

Amazon CloudWatch is used for:

- Viewing Lambda execution logs.
- Monitoring function execution.
- Troubleshooting application errors.
- Identifying failed requests.

## API Testing

The API was tested using Postman.

The following operations were tested:

- Create Employee
- Get All Employees
- Get Employee by ID
- Update Employee
- Delete Employee

## Key Learning Outcomes

Through this hands-on project, I learned:

- How Amazon API Gateway works.
- How to create an HTTP API.
- How API Gateway integrates with AWS Lambda.
- How to develop Lambda functions using Python.
- How to connect Lambda with DynamoDB using Boto3.
- How IAM roles and permissions work.
- How to perform CRUD operations.
- How to handle JSON requests and responses.
- How to troubleshoot API Gateway and Lambda errors.
- How to monitor Lambda execution using CloudWatch.
- How to test APIs using Postman.

## Future Enhancements

- Input validation.
- Environment variables.
- Improved error handling.
- DynamoDB pagination.
- JWT authentication and authorization.
- API throttling.
- CloudWatch alarms.
- Improved API security.

## Project Information

**Project Name:** AWS API Gateway Employee Management System

**Project Level:** Intermediate

**Cloud Provider:** Amazon Web Services

**Programming Language:** Python

**Database:** Amazon DynamoDB

**API Type:** API Gateway HTTP API

**Testing Tool:** Postman

---

This project was developed as part of my hands-on learning journey in AWS Cloud Engineering and Serverless Architecture.
