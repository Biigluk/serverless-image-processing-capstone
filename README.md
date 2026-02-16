# Serverless Image Processing Pipeline (Capstone)

## Overview

This project demonstrates a **serverless image processing pipeline** built using **AWS S3, Lambda, Step Functions, and API Gateway**.  
It shows how multiple AWS services can work together in an event-driven workflow without managing servers.

---

## How It Works

1. A client sends a **POST request** to API Gateway with an image key.
2. API Gateway triggers a **Step Functions** workflow.
3. Step Functions invokes a **Lambda function**.
4. Lambda reads an image from an **original S3 bucket** and writes a processed version to a **resized S3 bucket**.
5. The workflow returns **Success** or **Fail** based on execution results.

---

## AWS Resources Used

- **S3 Buckets**
  - `lukman-original-images-capstone`
  - `lukman-resized-images-capstone`

- **Lambda Function**
  - `ImageResizeFunction` (Python 3.x)
  - Simulates image resizing by copying and renaming files

- **Step Functions**
  - `ImageProcessingStateMachine`
  - Handles success and failure logic

- **API Gateway**
  - Accepts POST requests and starts the workflow

---

## Example Input
```json
{
  "key": "club2.png"
}
Example Output
{
  "success": true,
  "resized_key": "thumb-club2.png"
}

Architecture
Client
  ↓
API Gateway
  ↓
Step Functions
  ↓
Lambda
  ↓
S3 Original Bucket → S3 Resized Bucket

 Author
Lukman Ibrahim
Business Information Systems Student
Saskatchewan Polytechnic
