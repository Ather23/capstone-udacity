"""
SQL statements for bike share data
"""

create_dim_bike_trips_table = """
CREATE TABLE "public"."dim_bike_trips_table"
(
 "trip_id"       varchar(max) NOT NULL,
 "trip_duration" integer,
 "bike_id"       integer,
 "birth_year"    integer,
 "gender"        integer,
 "start_time"    timestamp NOT NULL,
 "end_time"      timestamp NOT NULL,
 CONSTRAINT "PK_dim_bike_trips_table" PRIMARY KEY ( "trip_id" )
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
    trip_id,
    trip_duration,
    start_time,
    end_time,
    bike_id,
    gender
)
SELECT 
    md5(starttime || bikeid) tripid,
    tripduration,
    starttime,
    stoptime,
    bikeid,
    gender
FROM bike_share_staging
WHERE 
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
