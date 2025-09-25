# Serverless-AI-Art-Generator

Serverless AI Art Generator
Project Overview
This project is a serverless application built on AWS Lambda that leverages the power of generative AI to create unique images from text prompts. It integrates with Amazon Bedrock to access a powerful text-to-image model (Stable Diffusion XL) and utilizes Amazon S3 for secure image storage.

The core functionality is an automated workflow that takes a text prompt, sends it to the AI model for image generation, and then saves the final image to a secure cloud bucket, providing a temporary link for viewing. This demonstrates an end-to-end serverless pipeline for an AI-powered service.

Key Features
Generative AI Integration: Uses the Stable Diffusion XL model on Amazon Bedrock to transform text descriptions into high-quality images.

Serverless Architecture: Deployed on AWS Lambda, ensuring a cost-effective, scalable, and maintenance-free solution.

Automated Workflow: The process from prompt input to image output and secure storage is fully automated.

Secure Storage: Generated images are stored in a private Amazon S3 bucket, with access controlled via programmatically generated pre-signed URLs.

Technologies Used
AWS Lambda: The serverless compute service hosting the application logic.

Amazon Bedrock: The fully managed service that provides access to foundation models.

Amazon S3: Used for scalable and secure storage of the generated images.

Python: The programming language used for the Lambda function.

Boto3: The AWS SDK for Python, used to interact with AWS services.

How It Works
A user's text prompt is sent to the AWS Lambda function.

The Lambda function uses Boto3 to send the prompt to the Stable Diffusion XL model on Amazon Bedrock.

The model generates an image, and the Lambda function receives the image data as a Base64-encoded string.

The function decodes the image, uploads the binary data to a specified S3 bucket, and assigns it a unique, timestamp-based filename.

Finally, a pre-signed URL is generated for the newly created S3 object, allowing for temporary and secure viewing of the image. This URL is returned to the user.

Setup and Deployment
AWS Account: Ensure you have an active AWS account with the necessary permissions for Lambda, Bedrock, and S3.

S3 Bucket: Create an S3 bucket to store the images. You will need to update the S3_BUCKET_NAME variable in the code with your bucket name.

Lambda Function:

Create a new Lambda function in the AWS Console.

Set the runtime to Python.

Paste the provided code into the Lambda function's code editor.

Configure an IAM role for the function that allows bedrock:InvokeModel and s3:PutObject permissions.

Testing: You can test the function directly from the AWS Lambda console by providing a JSON payload with your text prompt:
