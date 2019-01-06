import time

class Transcribe:

    COMPLETE_STATE = 'READY'
    PENDING_STATE = 'PENDING'

    def __init__(self, trans_client):
        self.client = trans_client

    def does_vocab_exist(self, name):
        # todo finish start job
     ###   response = self.client.start_transcription_job(
            TranscriptionJobName='string',
            LanguageCode='en-US' | 'es-US' | 'en-AU' | 'fr-CA' | 'en-GB' | 'de-DE' | 'pt-BR' | 'fr-FR' | 'it-IT',
            MediaSampleRateHertz=123,
            MediaFormat='mp3' | 'mp4' | 'wav' | 'flac',
            Media={
                'MediaFileUri': 'string'
            },
            OutputBucketName='string',
            Settings={
                'VocabularyName': 'string',
                'ShowSpeakerLabels': True | False,
                'MaxSpeakerLabels': 123,
                'ChannelIdentification': True | False
            }
        )
    ###

    def create_settings(self, name, locale, phrases):
        settings = {}
        # todo add settings conditionally
        return response['VocabularyName']

    def start_transcription(self, name, locale, phrases):
        settings = self.create_settings()

