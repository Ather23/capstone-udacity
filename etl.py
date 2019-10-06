from app_config import AppConfig
from constants import Tables
from query_dwh_tables import TableOperations
from s3_explorer import S3Helper
from stage_data import StageS3toRedShift
import logging


def create_tables():
    """
    Creates all tables for the
    dwh scheme
    :return: NONE
    """
    dwh = TableOperations()
    try:
        dwh.create_collision_tables()
        dwh.create_bike_share_tables()
        dwh.create_fact_tables()
    except Exception as e:
        assert False


def drop():
    """
    Drops all tables in dwh
    :return: None
    """
    dwh = TableOperations()
    dwh.drop_all_tables()


def stage_from_s3_to_redshift():
    """
    Imports all csv files from s3
    into redshift
    :return:
    """
    app = AppConfig()
    s3_exp = S3Helper()

    bike_share_data = s3_exp.get_all_file_name_from_key('bike-share')
    StageS3toRedShift(
        "bike_share_staging",
        app.s3_bucket, bike_share_data
    ).execute()

    collision_data = s3_exp.get_all_file_name_from_key('collision')
    StageS3toRedShift(
        "collision_staging",
        app.s3_bucket, collision_data
    ).execute()

    validate_tables([
        Tables.COLLISION_SHARING_TABLE_NAME,
        Tables.BIKE_SHARING_TABLE_NAME
    ])


def validate_tables(tbl_list):
    """
    Validates if tables have data
    :param tbl_list: list of table names
    :return: None
    """
    dwh = TableOperations()
    for tbl in tbl_list:
        count = dwh.row_count_table(tbl)
        if count < 1:
            raise Exception("{} has no rows".format(tbl))

def create_fact_dim_tables():
    """
    Creates fact and dim tables
    from staging tables
    :return:
    """
    dwh = TableOperations()
    try:
        dwh.insert_fact_and_dim_tables()
    except Exception as e:
        logging.critical(e)

    validate_tables([
        Tables.DIM_BIKE_TRIPS,
        Tables.DIM_STATION_TABLE,
        Tables.DIM_ZIP_CODE_TABLE,
        Tables.DIM_COLLISION_TABLE,
        Tables.FACT_TABLE_NAME
    ])


if __name__ == "__main__":
    drop()
    stage_from_s3_to_redshift()
    create_fact_dim_tables()
