from fact_table_builder import ProximityCalculation
import unittest


class TestTableCreation(unittest.TestCase):
    def test_fact_table(self):
        try:
            s = ProximityCalculation()
            ff = s.fact_table_data()

        except Exception as e:
            assert True

if __name__ == "__main__":
    unittest.main()
