import json
from s3_helper import S3Helper
from vocabulary_helper import Transcribe
from app import Vocab
import boto3
import botocore
import os
from transcription_helper import Helper
from transcribe_app import Transcribe

transcribe_client = boto3.client('transcribe')
s3_client = boto3.client("s3",
                         config=botocore.client.Config(signature_version='s3v4')
                         )
locale = os.environ['locale']
vocab = os.environ.get('vocab', "")
channel_ID = os.environ['Channel']
max_speakers = os.environ['Speakers']
output_bucket = os.environ['output']

def lambda_handler(event, context):
    speakers = 0
    if max_speakers.isnumeric():
        speakers = int(max_speakers)
    config = {
        'output': output_bucket,
        'VocabularyName': vocab,
        'MaxSpeakerLabels': speakers,
        'ChannelIdentification': channel_ID
    }
    trans_helper = Helper(transcribe_client,config)
    trans_creator = Transcribe(trans_helper, event)
    try:
        trans_creator.create_transcription()
    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)
        raise e
    return {
        "statusCode": 200,
        "body": json.dumps("Transcription submitted")
    }
