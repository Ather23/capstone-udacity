from red_shift_connection import RedShiftConnection
import validation_sql
import bike_share_sql_tables
import collision_sql_tables
import logging


class TableOperations:
    """
    Operations class for performing
    sql executions
    """

    def __init__(self):
        self.rds = RedShiftConnection()

    def __exec_sql_qry(self, queries):
        for qry in queries:
            try:
                self.rds.execute_sql(qry)
            except Exception as e:
                logging.critical("Query: {} | Error: {}".format(qry, e))
                raise Exception("Unable to execute query:{}".format(qry))

    def drop_all_tables(self):
        qrys = [
            "drop table IF EXISTS dim_station_table;",
            "drop table IF EXISTS fact_bike_trips_table;",
            "drop table IF EXISTS dim_zip_code_table;",
            "drop table IF EXISTS dim_street_table;",
            "drop table IF EXISTS fact_bike_accident_table;"
            # "drop table IF EXISTS street_table;",
            # "drop table IF EXISTS zip_code_table;",
        ]

        self.__exec_sql_qry(qrys)

    def create_bike_share_tables(self):
        tables_to_create = [
            bike_share_sql_tables.create_bike_share_staging,
            bike_share_sql_tables.create_dim_station_table
        ]
        self.__exec_sql_qry(tables_to_create)

    def create_collision_tables(self):
        tables_to_create = [
            collision_sql_tables.create_dim_zip_code_table,
            collision_sql_tables.create_dim_collision_table,
            collision_sql_tables.create_collision_staging,
            bike_share_sql_tables.create_dim_station_table,
            bike_share_sql_tables.create_dim_bike_trips_table
        ]
        self.__exec_sql_qry(tables_to_create)

    def create_fact_tables(self):
        tables_to_create = [
            collision_sql_tables.create_fact_bike_accident_table,
        ]

        self.__exec_sql_qry(tables_to_create)

    def insert_fact_and_dim_tables(self):
        tbls_to_insert = [
            bike_share_sql_tables.insert_dim_bike_trips_table,
            bike_share_sql_tables.insert_end_station_table,
            bike_share_sql_tables.insert_start_station_table,
            collision_sql_tables.insert_zip_codes,
            collision_sql_tables.insert_casualty_table
        ]
        self.__exec_sql_qry(tbls_to_insert)

    def row_count_table(self, table_name):
        qry = validation_sql.validation_count.format(table_name)
        qry = qry.format(table_name).strip()
        cur = self.rds.con.cursor()
        v = cur.execute(qry)
        x = v.fetchone()
        return self.rds.execute_sql([qry])
