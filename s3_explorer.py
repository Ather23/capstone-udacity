from app_config import AppConfig
import logging
import boto3


class S3Helper:
    """
    Helper class to has methods
    for files in s3
    """
    bucket_name = AppConfig().s3_bucket

    def __init__(self):
        super(S3Helper, self).__init__()
        s3 = boto3.resource('s3')
        self.bucket = s3.Bucket(self.bucket_name)

    def get_all_file_name_from_key(self, key):
        file_names = []
        objs = self.bucket.objects.filter(Prefix=key)
        for obj_summary in objs:
            try:
                if obj_summary.key == key: continue
                file_name = obj_summary.key
                file_names.append(file_name)
            except Exception as e:
                logging.critical(e)
                continue
        return file_names
