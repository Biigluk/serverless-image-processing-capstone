\# Serverless Image Processing Pipeline (Capstone)



\## Overview



This project implements a serverless image processing pipeline using AWS S3, Lambda, Step Functions, and API Gateway.



The pipeline works like this:



1\. A client sends a POST request to API Gateway with the image key.

2\. API Gateway starts a Step Functions execution.

3\. Step Functions invokes a Lambda function.

4\. Lambda reads an image from the \*\*original S3 bucket\*\*, processes it, and writes it into the \*\*resized S3 bucket\*\*.

5\. Step Functions returns Success or Fail based on Lambda output.



---



\## S3 Buckets



\- Original bucket: `lukman-original-images-capstone`

\- Resized bucket: `lukman-resized-images-capstone`



---



\## Lambda Function



\*\*ImageResizeFunction\*\*  

Runtime: Python 3.x



Input example:



```json

{

&nbsp; "key": "club2.png"

}

```



Output example:



```json

{

&nbsp; "success": true,

&nbsp; "resized\_key": "thumb-club2.png"

}

```



This function copies and renames the image to simulate resizing.



---



\## Step Functions State Machine



Name: `ImageProcessingStateMachine`



States:

\- \*\*ResizeImage\*\* → invokes Lambda

\- \*\*WasResizeSuccessful\*\* → choice state checking `success == true`

\- \*\*SuccessState\*\* → succeed

\- \*\*FailState\*\* → fail



This meets all required steps in the assignment.



---



\## API Gateway



Endpoint example:



```

POST https://vgzfzl7vr3.execute-api.ca-central-1.amazonaws.com/prod/process

```



Mapping template:



```vtl

{

&nbsp; "stateMachineArn": "arn:aws:states:ca-central-1:251941721502:stateMachine:ImageProcessingStateMachine",

&nbsp; "input": "$util.escapeJavaScript($input.body)"

}

```



---



\## Testing



1\. Upload `club2.png` to:

&nbsp;  - `lukman-original-images-capstone`



2\. Call the API with:

&nbsp;  ```json

&nbsp;  {

&nbsp;    "key": "club2.png"

&nbsp;  }

&nbsp;  ```



3\. Verify:

&nbsp;  - Step Functions execution = \*\*Succeeded\*\*

&nbsp;  - Resized bucket contains:

&nbsp;    - `thumb-club2.png`



---



\## Architecture Diagram



```

Client → API Gateway POST /process

&nbsp;       ↓

Step Functions (ImageProcessingStateMachine)

&nbsp;       ↓

Lambda (ImageResizeFunction)

&nbsp;       ↓

S3 Original Bucket → S3 Resized Bucket

```



