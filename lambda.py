# Firts Lambda function

import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""

    # Get the s3 address from the Step Function event input
    key = event['s3_key'] # file path
    bucket = event['s3_bucket'] # s3 bucket

    # Download the data from s3 to /tmp/image.png
    s3=boto3.resource('s3')
    s3.Object(bucket, key).download_file('/tmp/image.png')
    # s3.download_file(bucket, key, "/tmp/image.png")

    # Read the data from the local file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }

# Second Lambda function

import os
import io
import boto3
import json
import base64

# grab environment variables
ENDPOINT_NAME = 'scones-bike-motorcycle-classifier-2023-04-03-04-50'
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):

    # Grab the image_data from the event
    # Use this while attaching this lambda into Step Function. 
    
    image = base64.b64decode(event["body"]["image_data"])
    
    # Instantiate a Predictor
    runtime = boto3.client('runtime.sagemaker')
    
    # Make a prediction:
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME, ContentType="image/png",Body=image)
    inferences = json.loads(response['Body'].read().decode('utf-8'))
    print("...inferences:", inferences)
    # We return the data back to the Step Function    
    return {
        'statusCode': 200,
        'body': {
            "inferences": inferences
        }
    }

# Third Lambda function

import json


THRESHOLD = .93


def lambda_handler(event, context):
    
    # Grab the inferences from the event
    
    inferences = event['body']["inferences"]## TODO: fill in
    
    # Check if any values in our inferences are above THRESHOLD
    
    meets_threshold = False ## TODO: fill in
    for i in inferences:
        if i >= THRESHOLD:
            meets_threshold = True
            
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
