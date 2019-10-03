from query_dwh_tables import TableOperations
import unittest

class TestTableCreation(unittest.TestCase):
    def test_create_bike_share_tables_should_not_throw_exception(self):
        dwh = TableOperations()
        try:
            dwh.create_bike_share_tables()
        except Exception as e:
            assert False

    def test_create_collision_tables_should_not_throw_exception(self):
        dwh = TableOperations()
        try:
            dwh.create_collision_tables()
        except Exception as e:
            assert False

    def test_row_count(self):
        dwh = TableOperations()
        try:
            obj = dwh.row_count_table("bike_share_staging")
            print(obj)
        except Exception as e:
            assert False


if __name__ == "__main__":
    unittest.main()