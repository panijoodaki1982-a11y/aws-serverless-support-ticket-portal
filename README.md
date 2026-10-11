# AWS Serverless Support Ticket Portal ☁️

A hands-on AWS cloud project demonstrating how to build a serverless support ticket submission application using Amazon S3, Amazon API Gateway, AWS Lambda, Python, and Amazon DynamoDB.

## Project Overview

This project allows users to submit support tickets through a web interface. Requests are processed by a Python-based AWS Lambda function and stored in Amazon DynamoDB.

The project was developed as part of my practical AWS cloud learning journey, focusing on cloud architecture, API integration, serverless computing, troubleshooting, and database operations.

## Architecture

Frontend (Amazon S3) → API Gateway → AWS Lambda (Python) → Amazon DynamoDB

## AWS Services Used


| AWS Service | Purpose |
|---|---|
| Amazon S3 | Static website hosting |
| API Gateway | HTTP API for support tickets |
| AWS Lambda | Serverless Python backend |
| DynamoDB | Support ticket storage |
| CloudWatch | Monitoring and logs |
| AWS IAM | Access and permissions |
  

## Features

* Responsive web form for submitting support tickets
* API Gateway integration with AWS Lambda
* Python backend using Boto3
* JSON request parsing and input validation
* Unique ticket IDs generated using UUID
* Automatic ticket timestamps
* Ticket storage in DynamoDB
* Default ticket status: OPEN
* HTTP response codes for successful and invalid requests
* CORS configuration for browser-to-API communication

## How It Works

1. A user enters their name, email address, and support issue.
2. The frontend sends a POST request to the /tickets API endpoint.
3. API Gateway invokes the AWS Lambda function.
4. Lambda validates the request and generates a unique ticket ID.
5. The ticket is stored in the DynamoDB SupportTickets table.
6. The API returns a successful response to the frontend.

## Testing and Troubleshooting

The application was successfully tested using the AWS Management Console and the web interface.

Key activities included:

* Testing Lambda with sample JSON requests
* Troubleshooting browser Failed to fetch errors
* Configuring CORS and the Content-Type request header
* Correcting JSON body parsing in Lambda
* Verifying successful HTTP 201 responses
* Confirming ticket records in DynamoDB
* Validating stored name, email, issue, timestamp, and status fields

## Repository Structure

* index.html — Frontend application
* lambda_function.py — Python Lambda backend
* README.md — Project documentation

## Deployment Notes

To redeploy this project:

1. Create a DynamoDB table named SupportTickets with ticketId as its string partition key.
2. Create an AWS Lambda function using the provided Python code.
3. Configure the Lambda execution role with the required DynamoDB permissions.
4. Create an HTTP API in API Gateway with a POST /tickets route integrated with Lambda.
5. Configure appropriate CORS settings.
6. Update the API endpoint in index.html.
7. Deploy the frontend using Amazon S3 static website hosting.

For production use, additional authentication, stricter CORS settings, monitoring, and abuse protection would be required.

## Project Status

Successfully developed and tested.

The cloud resources used for the demonstration have been deleted to avoid ongoing AWS charges. The source code remains available in this repository for learning, review, and future redeployment.

## Skills Demonstrated

AWS Cloud Architecture · Serverless Computing · Python · REST APIs · DynamoDB · IAM · Cloud Troubleshooting · JSON · CORS · AWS Cost Awareness

⸻

Project type: Personal AWS Cloud Portfolio Project

Focus: Junior Cloud Engineer / AWS Cloud Support / Cloud Operations
