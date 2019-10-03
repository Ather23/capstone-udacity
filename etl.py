from app_config import AppConfig
from query_dwh_tables import TableOperations
from s3_explorer import S3Helper
from stage_data import StageS3toRedShift


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
        assert False


if __name__ == "__main__":

    #create_tables()
    stage_from_s3_to_redshift()
    create_fact_dim_tables()
