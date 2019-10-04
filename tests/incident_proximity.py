from StationProximityCalculation import ProximityCalculation
from query_dwh_tables import TableOperations
import unittest

class TestTableCreation(unittest.TestCase):
    def test_fact_table(self):
        s = ProximityCalculation()
        ff = s.fact_table_data()
if __name__ == "__main__":
    unittest.main()