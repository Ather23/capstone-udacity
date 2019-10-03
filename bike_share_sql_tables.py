"""
SQL statements for bike share data
"""

create_station_table = """
CREATE TABLE IF NOT EXISTS dim_station_table (
    station_id INTEGER PRIMARY KEY,
    station_name VARCHAR(MAX),
    longitude DECIMAL(10,7),
    latitude DECIMAL(10,7)
);
"""

create_bike_trip_table = """
CREATE TABLE IF NOT EXISTS fact_bike_trips_table (
    trip_id INTEGER NOT NULL,
    trip_duration INTEGER,
    start_station_id INTEGER NOT NULL,
    end_station_id INTEGER NOT NULL,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    bike_id INTEGER,
    birth_year INTEGER,
    gender INTEGER,
    CONSTRAINT biketrips_pkey PRIMARY KEY (trip_id)
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

###INSERT

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
