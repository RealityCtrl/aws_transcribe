import time

class Transcribe:

    COMPLETE_STATE = 'READY'
    PENDING_STATE = 'PENDING'

    def __init__(self, trans_client):
        self.client = trans_client

    def does_vocab_exist(self, name):
        response = self.client.list_vocabularies(
            NameContains='name'
        )
        print(response)
        for vocab in response['Vocabularies']:
            if vocab['VocabularyName'] == name:
                return True
        return False

    def create_vocab(self, name, locale, phrases):
        response = self.client.create_vocabulary(
            VocabularyName=name,
            LanguageCode=locale,
            Phrases=phrases
        )
        print(response)
        return response['VocabularyName']

    def check_for_completion(self, name):
        status_response = self.get_status(name)
        print(status_response)
        if status_response['VocabularyState'] == self.COMPLETE_STATE:
            return True
        elif status_response['VocabularyState'] == self.PENDING_STATE:
            return False
        else:
            print("Vocab {0} update/creation failed due to {1}".format(name,status_response['FailureReason']))
            raise Exception()

    def get_status(self, name):
        response = self.client.get_vocabulary(
            VocabularyName='string'
        )
        return response

    def update_vocab(self, name, locale, phrases):
        response = self.client.update_vocabulary(
            VocabularyName=name,
            LanguageCode=locale,
            Phrases=phrases
        )
        print(response)
        return response['VocabularyName']

    def insert_update_vocab(self, name, locale, phrases):
        if self.does_vocab_exist:
            vocab_name = self.update_vocab(name, locale, phrases)
        else:
            vocab_name = self.create_vocab(name, locale, phrases)
        is_complete = self.check_for_completion(vocab_name)
        while not is_complete:
            time.sleep(5)
            is_complete = self.check_for_completion(vocab_name)
        return vocab_name
