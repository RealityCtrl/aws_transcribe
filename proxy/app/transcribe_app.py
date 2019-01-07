from botocore.exceptions import ClientError
from time import sleep


class Transcribe:

    def __int__(self, trans_helper, event):
        self.trans_helper = trans_helper
        self.event = event

    def create_transcription(self):
        bucket = self.get_bucket_name(self.event)
        name = self.get_object_name(self.event)
        file_type = self.get_file_type(self.event)
        self.submit_transcription(bucket, name, file_type)

    def submit_transcription(self, bucket, name, file_type):
        try:
            response = self.trans_helper.start_transcription(bucket, name, file_type)
        except ClientError as ex:
            if ex['Error']['Code'] == 'LimitExceededException':
                sleep(15)
                return self.submit_transcription(bucket, name, file_type)
            else:
                print(ex)
                raise ex
        if response['TranscriptionJobStatus'] == 'FAILED':
            print("failed: "+response['FailureReason'])
        else:
            print(response)


    def get_bucket_name(self, event):
        return event['Records'][0]['s3']['bucket']['name']

    def get_object_name(self, event):
        return event['Records'][0]['s3']['object']['key']

    def get_file_type(self, event):
        key = self.get_object_name(event)
        return key.substring(key.rfind('.'), -1)
