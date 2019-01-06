import json
from s3_helper import S3Helper
from vocabulary_helper import Transcribe
from app import Vocab
import boto3
import botocore
import os

transcribe_client = boto3.client('transcribe')
s3_client = boto3.client("s3",
                         config=botocore.client.Config(signature_version='s3v4')
                         )
locale = os.environ['locale']

def lambda_handler(event, context):
    trans_helper = Transcribe(transcribe_client)
    vocab_creator = Vocab(trans_helper, object_helper, event)
    try:
        response_body = vocab_creator.create_vocab()
    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)
        raise e
    return {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }
