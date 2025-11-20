import boto3
import os

s3 = boto3.client('s3')

ORIGINAL_BUCKET = "lukman-original-images-capstone"
RESIZED_BUCKET = "lukman-resized-images-capstone"

def lambda_handler(event, context):
    image_key = event.get("key")

    if not image_key:
        return {
            "success": False,
            "errorMessage": "No 'key' found in event"
        }

    try:
        resized_key = f"thumb-{os.path.basename(image_key)}"

        s3.copy_object(
            Bucket=RESIZED_BUCKET,
            Key=resized_key,
            CopySource={
                "Bucket": ORIGINAL_BUCKET,
                "Key": image_key
            }
        )

        return {
            "success": True,
            "original_key": image_key,
            "resized_key": resized_key
        }

    except Exception as e:
        return {
            "success": False,
            "errorMessage": str(e)
        }
