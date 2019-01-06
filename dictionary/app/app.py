class Vocab:

    def __int__(self, trans_helper, s3_helper, event):
        self.trans_helper = trans_helper
        self.s3_helper = s3_helper
        self.event = event

    def create_vocab(self, locale):
        phrases = self.get_phrases(self.event)
        name = self.get_object_name(self.event)
        self.trans_helper.start_transcription(name, locale, phrases)

    def get_phrases(self, event):
        bucket_name = self.get_bucket_name(event)
        object_name = self.get_object_name(event)
        phrases = self.s3_helper.download_object(bucket_name, object_name)
        print(phrases)
        return phrases

    def get_bucket_name(self, event):
        return event['Records'][0]['s3']['bucket']['name']

    def get_object_name(self, event):
        return event['Records'][0]['s3']['object']['key']

