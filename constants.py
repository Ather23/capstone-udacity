class Tables:
    BIKE_SHARING_TABLE_NAME = "bike_share_staging"
    COLLISION_SHARING_TABLE_NAME = "collision_staging"

    FACT_TABLE_NAME = "fact_trip_incident_table"

    DIM_BIKE_TRIPS = "dim_bike_trips_table"
    DIM_STATION_TABLE = "dim_station_table"
    DIM_ZIP_CODE_TABLE = 'dim_zip_code_table'
    DIM_COLLISION_TABLE="dim_collision_table"

    def __init__(self):
        super(Tables, self).__init__()
