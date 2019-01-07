import time

class Transcribe:

    COMPLETE_STATE = 'READY'
    PENDING_STATE = 'PENDING'

    def __init__(self, trans_client, config):
        self.client = trans_client
        self.config = config

    def start_job(self, name, file_type, uri, settings):
        response = self.client.start_transcription_job(
            TranscriptionJobName=name,
            LanguageCode=self.config['locale'],
            MediaFormat=file_type,
            Media={
                'MediaFileUri': uri
            },
            OutputBucketName=self.config['output'],
            Settings=settings
        )
        return response

    def create_uri(self, bucket, name):
        return "https://s3.amazonaws.com/"+bucket+"/"+name

    def create_settings(self):
        settings = {}
        if self.config['VocabularyName'] != "":
            settings['VocabularyName'] = self.config['VocabularyName']
        if self.config['MaxSpeakerLabels'] >=2:
            settings['MaxSpeakerLabels'] = self.config['MaxSpeakerLabels']
            settings['ShowSpeakerLabels'] = True
        elif self.config['ChannelIdentification'] == "True":
            settings['ChannelIdentification'] = True
        return settings

    def start_transcription(self, bucket_name, name, file_type):
        settings = self.create_settings()
        uri = self.create_uri(bucket_name, name)
        response = self.start_job(name, file_type, uri, settings)
        return response

