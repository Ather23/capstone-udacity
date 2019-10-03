"""
SQL tables for collision schema
"""

create_dim_zip_code_table = """
CREATE TABLE IF NOT EXISTS "public"."dim_zip_code_table" 
(
 "zip_code"  varchar(256) NOT NULL,
 "longitude" decimal(10,7) NOT NULL,
 "latitude"  decimal(10,7) NOT NULL,
 "borough"   varchar(max) NOT NULL,
 CONSTRAINT "PK_dim_zip_code_table" PRIMARY KEY ( "zip_code" )
);
"""
create_dim_collision_table = """
CREATE TABLE IF NOT EXISTS "public"."dim_collision_table"
(
 "unique_id"                     integer NOT NULL,
 "total_persons_killed"          integer,
 "total_persons_injured"         integer,
 "total_cyclists_killed"         integer,
 "total_cyclists_injured"        integer,
 "total_motorists_injured"       integer,
 "total_motorists_killed"        integer,
 "contributing_factor_vehicle_1" varchar(max),
 "contributing_factor_vehicle_2" varchar(max),
 "contributing_factor_vehicle_3" varchar(max),
 "contributing_factor_vehicle_4" varchar(max),
 "contributing_factor_vehicle_5" varchar(max),
 "vehicle_type_code_1"           varchar(max),
 "vehicle_type_code_2"           varchar(max),
 "vehicle_type_code_3"           varchar(max),
 "vehicle_type_code_4"           varchar(max),
 "vehicle_type_code_5"           varchar(max),
 "on_street_name"                varchar(max),
 "cross_street_name"             varchar(max),
 "off_street_name"               varchar(max),
 "timestamp"                     timestamp NOT NULL,
 CONSTRAINT "PK_dim_collision_table" PRIMARY KEY ( "unique_id" )
);
"""
create_fact_bike_accident_table = """
CREATE TABLE "public"."fact_bike_accident_table"
(
 "trip_id"          integer IDENTITY ( 1, 1 ),
 "unique_id"        integer,
 "start_station_id" integer NOT NULL,
 "zip_code"         varchar(256) NOT NULL,
 "end_station_id"   integer NOT NULL,
 CONSTRAINT "PK_fact_bike_accident_table" PRIMARY KEY ( "trip_id" )
);
"""
create_collision_staging = """
CREATE TABLE IF NOT EXISTS collision_staging(
    date VARCHAR(100),
    time VARCHAR(100),
    borough VARCHAR(MAX),
    zip_code VARCHAR(MAX),
    latitude decimal(10,7),
    longitude decimal(10,7),
    location VARCHAR(MAX),
    on_street_name VARCHAR(MAX),
    cross_street_name VARCHAR(MAX),
    off_street_name VARCHAR(MAX),
    number_of_persons_injured INTEGER,
    number_of_persons_killed INTEGER,
    number_of_pedestrians_injured INTEGER,
    number_of_pedestrians_killed INTEGER,
    number_of_cyclists_injured INTEGER,
    number_of_cyclists_killed INTEGER,
    number_of_motorist_injured INTEGER,
    number_of_motorist_killed INTEGER,
    contributing_factor_vehicle_1 VARCHAR(MAX),
    contributing_factor_vehicle_2 VARCHAR(MAX),
    contributing_factor_vehicle_3 VARCHAR(MAX),
    contributing_factor_vehicle_4 VARCHAR(MAX),
    contributing_factor_vehicle_5 VARCHAR(MAX),
    unique_id INTEGER,
    vehicle_type_code_1 VARCHAR(MAX),
    vehicle_type_code_2 VARCHAR(MAX),
    vehicle_type_code_3 VARCHAR(MAX),
    vehicle_type_code_4 VARCHAR(MAX),
    vehicle_type_code_5 VARCHAR(MAX)
);
"""

insert_casualty_table = """
INSERT INTO dim_collision_table (
    unique_id,
    total_persons_killed,
    total_persons_injured,
    total_cyclists_killed,
    total_cyclists_injured,
    total_motorists_injured,
    total_motorists_killed,
    contributing_factor_vehicle_1,
    contributing_factor_vehicle_2,
    contributing_factor_vehicle_3,
    contributing_factor_vehicle_4,
    contributing_factor_vehicle_5,
    vehicle_type_code_1,
    vehicle_type_code_2,
    vehicle_type_code_3,
    vehicle_type_code_4,    
    vehicle_type_code_5,
    on_street_name,
    cross_street_name,
    off_street_name,
    timestamp
)
SELECT 
    distinct unique_id,
    number_of_persons_killed,
    number_of_persons_injured,
    number_of_cyclists_killed,
    number_of_cyclists_injured,
    number_of_motorist_injured,
    number_of_motorist_killed,
    contributing_factor_vehicle_1,
    contributing_factor_vehicle_2,
    contributing_factor_vehicle_3,
    contributing_factor_vehicle_4,
    contributing_factor_vehicle_5,
    vehicle_type_code_1,
    vehicle_type_code_2,
    vehicle_type_code_3,
    vehicle_type_code_4,
    vehicle_type_code_5,
    on_street_name,
    cross_street_name,
    off_street_name,
    {}
FROM 
    collision_staging as cs
WHERE
	longitude IS NOT NULL and
    zip_code IS NOT NULL and
    zip_code <> TRIM('');
""".format("TO_TIMESTAMP(cs.date+' '+cs.time,'MM/DD/YYYY HH:MI')")
insert_zip_codes = """
INSERT INTO dim_zip_code_table(
  zip_code,
  longitude,
  latitude,
  borough
)
SELECT
	distinct zip_code,
    longitude,
    latitude,
    borough
FROM
	collision_staging
WHERE
	longitude IS NOT NULL and
    zip_code IS NOT NULL and
    zip_code <> TRIM('');
"""
