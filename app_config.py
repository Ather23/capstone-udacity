import configparser

from Utilities import Utilities
import os


class AppConfig:
    """
    Wrapper class for fetching configuration
    details
    """
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path())
        self.user = self.config["AWS"]["DWH_DB_USER"]
        self.password = self.config["AWS"]["DWH_DB_PASSWORD"]
        self.endpoint = self.config["AWS"]["DWH_ENDPOINT"]
        self.port = self.config["AWS"]["DWH_PORT"]
        self.db = self.config["AWS"]["DWH_DB"]
        self.s3_bucket = self.config["S3"]["BUCKET_NAME"]
        self.aws_key = self.config["AWS"]["AWS_ACCESS_KEY_ID"]
        self.aws_secret = self.config["AWS"]["AWS_SECRET_ACCESS_KEY"]

    def config_path(self):
        utils = Utilities()
        path = "{}/app.config".format(utils.get_main_dir())
        if os.path.isfile(path) is False:
            raise FileNotFoundError("app.config")
        return path
