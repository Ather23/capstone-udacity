from app_config import AppConfig
import psycopg2


class RedShiftConnection:
    conn_string = """
    dbname='{}' port='{}' user='{}' password='{}' host='{}'
    """

    def __init__(self):
        super(RedShiftConnection, self).__init__()
        app = AppConfig()
        con_str = self.conn_string.format(
            app.db,
            app.port,
            app.user,
            app.password,
            app.endpoint
        )

        self.connection = psycopg2.connect(con_str)
        self.cursor = self.connection.cursor()
