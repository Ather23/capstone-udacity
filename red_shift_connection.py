import psycopg2

from app_config import AppConfig


class RedShiftConnection:
    """
    Handles redshift operations
    """

    def __init__(self):
        config = AppConfig()
        self.user = config.user
        self.password = config.password
        self.endpoint = config.endpoint
        self.port = config.port
        self.db = config.db
        self.conn_string = "dbname='{}' port='{}' user='{}' password='{}' host='{}'".format(self.db,
                                                                                            self.port,
                                                                                            self.user,
                                                                                            self.password,
                                                                                            self.endpoint)
        self.con = psycopg2.connect(self.conn_string)

    def execute_sql(self, query):
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def close(self):
        self.con.close()
