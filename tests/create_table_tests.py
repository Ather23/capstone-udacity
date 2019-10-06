from query_dwh_tables import TableOperations
import unittest

from red_shift_connection import RedShiftConnection


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

    def test_fetch_data(self):
        dwh = TableOperations()
        try:
            obj = dwh.fetch_data("""
                SELECT *
                FROM bike_share_staging
                LIMIT 5;
            """)
            print(obj)
        except Exception as e:
            assert False

    def test_bike_strips_query(self):
        bike_trips_query = """
            SELECT 
                md5(bikeid || starttime) as bike_trip_id,
                start_station_id,
                end_station_id,
                start_station_latitude,
                start_station_longitude,
                end_station_latitude,
                end_station_longitude     
            FROM 
            public.bike_share_staging

            WHERE
                start_station_latitude IS NOT NULL AND
                start_station_longitude IS NOT NULL
            limit 100;    
        """
        dwh = TableOperations()
        try:
            obj = dwh.fetch_data(bike_trips_query)
            print(obj)
        except Exception as e:
            assert False

    def test_insert_into_fact_tble(self):
        fact_insert = f"""
               INSERT INTO fact_trip_incident_table(
                   incident_id,
                   bike_id,
                   unique_id,
                   start_station_id,
                   end_station_id        
               ) VALUES (
                   {123},{123},{1},{2}
               )                
           """;

        tbl = TableOperations()
        tbl.execute_qry(fact_insert)

    def test_hashfunction(self):
        tbop = TableOperations()
        obj = tbop.md5_hash(14548, "2013-07-01 00:00:00")
        print(obj)


if __name__ == "__main__":
    unittest.main()
