from app_config import AppConfig
from red_shift_connection import RedShiftConnection
from Utilities import Utilities
import unittest


class TestAWSConnection(unittest.TestCase):
    def test_app_config_should_exist(self):
        print('Checking if app config exists')
        app = AppConfig()
        self.assertTrue(app.config_path())

    def test_config_parser(self):
        cfg = AppConfig().config
        for section in cfg.sections():
            print(section)
            for option in cfg.options(section):
                print(" ", option, "=", cfg.get(section, option))

    def test_connect_should_not_throw_exception(self):
        print("Checking RedShift connection")
        try:
            rds = RedShiftConnection()
            assert True
        except:
            assert (False, "Connection failed")

    def test_execute_sql_should_not_throw_exception(self):
        sql_create = """
                CREATE TABLE test_table_4(
                    testing_int INTEGER                 
                );
                """
        rds = RedShiftConnection()
        rds.execute_sql(sql_create)
        rds.close()

    def test_curr_dir(self):
        print(Utilities().get_main_dir())


if __name__ == "__main__":
    unittest.main()
