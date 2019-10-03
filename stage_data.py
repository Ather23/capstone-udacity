import logging
from app_config import AppConfig
from redshift_conn import RedShiftConnection


class StageS3toRedShift:
    copy_cmd = """
    COPY {} FROM 's3://{}/{}' 
    CREDENTIALS 'aws_access_key_id={};aws_secret_access_key={}' 
    CSV IGNOREHEADER 1; 
    """

    def __init__(self, table,
                 s3_bucket, s3_keys):
        super(StageS3toRedShift, self).__init__()
        self.s3_keys = s3_keys
        self.s3_bucket = s3_bucket
        self.table = table

    def execute(self):
        logging.info("Staging data from s3 for {}".format(self.table))
        count = 0
        app = AppConfig()
        rsc = RedShiftConnection()
        for key in self.s3_keys:
            try:
                cmd = self.copy_cmd.format(
                    self.table,
                    app.s3_bucket,
                    key,
                    app.aws_key,
                    app.aws_secret
                )
                rsc.cursor.execute(cmd)
                rsc.connection.commit()
                count += 1
            except Exception as e:
                logging.critical(e)
                rsc.connection.rollback()
                continue

        rsc.connection.close()
        if count < 1:
            logging.error("Unable to staging any data")
        else:
            logging.info("Staged {}/{} files".format(count,len(self.s3_keys)))
