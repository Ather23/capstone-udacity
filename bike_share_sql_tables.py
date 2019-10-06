"""
SQL statements for bike share data
"""

create_dim_bike_trips_table = """
CREATE TABLE IF NOT EXISTS "public"."fact_trip_incident_table"
(
 "start_station_id" integer NOT NULL,
 "biked_id"         integer IDENTITY ( 1, 1 ),
 "unique_id"        integer,
 "end_station_id"   integer NOT NULL,
 "zip_code"         varchar(max) NOT NULL,
 CONSTRAINT "PK_fact_bike_accident_table" PRIMARY KEY ( "start_station_id", "biked_id" )
);



"""
create_dim_station_table = """
CREATE TABLE IF NOT EXISTS "public"."dim_station_table"
(
 "station_id"   integer NOT NULL,
 "station_name" varchar(max) NOT NULL,
 "longitude"    decimal(10,7) NOT NULL,
 "latitude"     decimal(10,7) NOT NULL,
 CONSTRAINT "PK_dim_station_table" PRIMARY KEY ( "station_id" )
);
"""


create_bike_share_staging = """
    CREATE TABLE IF NOT EXISTS bike_share_staging(
        tripduration INTEGER,
        starttime TIMESTAMP,
        stoptime TIMESTAMP,
        start_station_id INTEGER,
        start_station_name VARCHAR(MAX),
        start_station_latitude DECIMAL(10,7),
        start_station_longitude DECIMAL(10,7),
        end_station_id INTEGER,
        end_station_name VARCHAR(MAX),
        end_station_latitude DECIMAL(10,7),
        end_station_longitude DECIMAL(10,7),
        bikeid INTEGER,
        usertype VARCHAR(MAX),
        birthyear INTEGER,
        gender INTEGER         
    );
"""

"""
INSERT statements
"""
insert_dim_bike_trips_table = """
INSERT INTO dim_bike_trips_table (
    bike_id,
    start_time,
    trip_duration,
    end_time,
    gender,
    birth_year
)
SELECT 
    bikeid,
    starttime,
    tripduration,
    stoptime,
    gender,
    birthyear
FROM bike_share_staging
WHERE 
    bikeid IS NOT NULL and
    starttime IS NOT NULL and
    start_station_longitude IS NOT NULL and 
    start_station_id IS NOT NULL and
    end_station_latitude IS NOT NULL and
    end_station_longitude IS NOT NULL; 
"""
insert_start_station_table = """
INSERT INTO dim_station_table (
    station_id,
    station_name,
    longitude,
    latitude
    )
SELECT 
    distinct start_station_id,
    start_station_name,
    start_station_longitude,
    start_station_latitude
FROM 
    bike_share_staging
WHERE 
    start_station_longitude IS NOT NULL and 
    start_station_id IS NOT NULL;
"""
insert_end_station_table = """
INSERT INTO dim_station_table (
    station_id,
    station_name,
    longitude,
    latitude
    )
SELECT 
    distinct start_station_id,
    end_station_name,
    end_station_longitude,
    end_station_latitude
FROM 
    bike_share_staging
WHERE 
    end_station_longitude IS NOT NULL and 
    end_station_id IS NOT NULL;
"""
