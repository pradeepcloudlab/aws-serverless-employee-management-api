
# AWS API Gateway Employee Management Project
# Project Documentation and Resource Inventory

## 1. Project Information

Project Name: AWS API Gateway Employee Management System

Project Level: Intermediate

Cloud Provider: AWS

AWS Region: ap-south-1 (Mumbai)

Programming Language: Python

API Type: HTTP API

Database: DynamoDB

Testing Tool: Postman

---

## 2. AWS Resource Inventory

### 2.1 IAM

| Configuration | Value |
|---|---|
| IAM Role Name | employee-lambda-role |
| Used By | AWS Lambda |
| Purpose | Allow Lambda to access DynamoDB |
| Service | Lambda |

### 2.2 AWS Lambda

| Configuration | Value |
|---|---|
| Function Name | employee-api-function |
| Runtime | Python 3.12 |
| Handler | lambda_function.lambda_handler |
| Execution Role | employee-lambda-role |
| Programming Language | Python |
| AWS Region | ap-south-1 |

Lambda Responsibilities:

- Receive API Gateway requests.
- Process employee information.
- Create employee records.
- Retrieve employee records.
- Update employee records.
- Delete employee records.
- Connect to DynamoDB using Boto3.
- Return JSON responses.

### 2.3 Amazon DynamoDB

| Configuration | Value |
|---|---|
| Table Name | Employees |
| Partition Key | employeeId |
| Key Type | String |
| AWS Region | ap-south-1 |

Purpose:

Store employee information.

### 2.4 Amazon API Gateway

| Configuration | Value |
|---|---|
| API Name | employee-management-api |
| API Type | HTTP API |
| Stage Name | dev |
| Integration | AWS Lambda |
| Lambda Function | employee-api-function |
| AWS Region | ap-south-1 |

API Base URL:

Paste your actual API Gateway invoke URL here.

---

## 3. API Routes

| Method | Route | Purpose |
|---|---|---|
| POST | /employees | Create employee |
| GET | /employees | Get all employees |
| GET | /employees/{id} | Get employee by ID |
| PUT | /employees/{id} | Update employee |
| DELETE | /employees/{id} | Delete employee |

---

## 4. Project Architecture

```plaintext
Client / Postman
       |
       v
Amazon API Gateway
       |
       v
AWS Lambda (Python)
       |
       v
Amazon DynamoDB
       |
       v
Employees Table
```
CloudWatch is used for logging and monitoring.

---

## 5. Project Setup Steps

### Stage 1: IAM Configuration
- Create IAM execution role.
- Configure DynamoDB permissions.
- Attach role to Lambda.

### Stage 2: DynamoDB Configuration
- Create Employees table.
- Configure employeeId as partition key.
- Select String as key type.

### Stage 3: Lambda Configuration
- Create employee-api-function.
- Select Python runtime.
- Configure IAM execution role.
- Write Python backend code.
- Connect Lambda to DynamoDB.

### Stage 4: API Gateway Configuration
- Create HTTP API.
- Configure Lambda integration.
- Create API routes.
- Create dev stage.
- Deploy API.

### Stage 5: API Testing
- Test POST employee.
- Test GET all employees.
- Test GET employee by ID.
- Test PUT employee.
- Test DELETE employee.

### Stage 6: GitHub
- Create GitHub repository.
- Upload Lambda code.
- Upload README documentation.
- Upload project notes.

---

## 6. Project Progress Tracker

- [x] IAM Role
- [x] DynamoDB Table
- [x] Lambda Function
- [x] API Gateway
- [x] POST Employee
- [x] GET All Employees
- [x] GET Employee by ID
- [x] PUT Employee
- [x] DELETE Employee
- [x] GitHub Upload
- [ ] Environment Variables
- [ ] DynamoDB Pagination
- [ ] Advanced Error Handling
- [ ] API Authentication
- [ ] API Throttling
- [ ] CloudWatch Monitoring
- [ ] CloudWatch Alarms
- [ ] Final Project Testing

---

## 7. Important Learning Notes

Store your important learning points here.

Example:

1. API Gateway receives HTTP requests.
2. Lambda executes backend code.
3. DynamoDB stores employee information.
4. IAM controls access between AWS services.
5. CloudWatch stores execution logs.

---

## 8. Troubleshooting Notes

Record issues and their solutions here.

| Issue | Solution |
|---|---|
| Decimal not JSON serializable | Convert DynamoDB Decimal values before JSON serialization |
| Route not found | Check API Gateway route configuration |
| Lambda 500 error | Check Lambda CloudWatch logs |
| Access denied | Check Lambda IAM permissions |

---

## 9. Important Security Notes

- Never store AWS access keys or secret keys in GitHub.
- Never upload passwords or credentials.
- Do not upload sensitive employee information.
- Keep IAM permissions limited to required actions.
- Do not publish sensitive account information.

---

## 10. Future Project Updates

Add new AWS resources and project changes here.

| Date | Change | Resource |
|---|---|---|
|  |  |  |

