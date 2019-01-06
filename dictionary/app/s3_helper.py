
class S3Helper:

    def __init__(self, s3client):
        self.s3client = s3client

    def download_object(self, bucket_name, key):
        bucket = self.s3client.Bucket(bucket_name)
        obj = bucket.Object(key)
        with open('vocab.txt', 'wb') as data:
            obj.download_fileobj(data)
            print(data)
            file_string = data.read().decode('utf-8')
            print(file_string)
        return file_string.split()


