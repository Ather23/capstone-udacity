from red_shift_connection import RedShiftConnection
import bike_share_sql_tables
import collision_sql_tables
import logging


class CreateDwhTables:
    def __init__(self):
        self.rds = RedShiftConnection()

    def __create_tables_from_queries(self,queries):
        for qry in queries:
            try:
                self.rds.execute_sql(qry)
            except Exception as e:
                raise Exception("Unable to execute query:{}".format(qry))

    def create_bike_share_tables(self):
        tables_to_create=[
            bike_share_sql_tables.create_bike_trip_table,
            bike_share_sql_tables.create_station_table,
            bike_share_sql_tables.create_user_table,
            bike_share_sql_tables.create_bike_share_staging
        ]
        self.__create_tables_from_queries(tables_to_create)

    def create_collision_tables(self):
        tables_to_create=[
            collision_sql_tables.create_collision_table,
            collision_sql_tables.create_casualty_table,
            collision_sql_tables.create_street_table,
            collision_sql_tables.create_zip_code_table,
            collision_sql_tables.crate_collision_staging
        ]
        self.__create_tables_from_queries(tables_to_create)
