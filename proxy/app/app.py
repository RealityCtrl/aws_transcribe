class Vocab:

    def __int__(self, trans_helper, event):
        self.trans_helper = trans_helper
        self.event = event

    def create_transcription(self):
        name = self.get_object_name(self.event)
        self.trans_helper.start_transcription(name)
        # todo finish event extraction logic + handle errors

    def get_bucket_name(self, event):
        return event['Records'][0]['s3']['bucket']['name']

    def get_object_name(self, event):
        return event['Records'][0]['s3']['object']['key']

    def get_file_type(self, event):
        return self.get_object_name(event).rfind('.')
