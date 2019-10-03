"""
COLLISION SCHEMA
"""

create_collision_table = """
CREATE TABLE IF NOT EXISTS collision_table(
    unique_id INTEGER,
    timestamp TIMESTAMP,
    zip_code INTEGER
);
"""

create_zip_code_table = """
CREATE TABLE IF NOT EXISTS zip_code_table(
    zip_code INTEGER,
    logitude DECIMAL(10,7),
    latitude DECIMAL(10,7),
    borough VARCHAR(MAX)
);
"""

create_street_table = """
CREATE TABLE IF NOT EXISTS street_table(
    unique_id INTEGER,
    on_street_name VARCHAR(MAX),
    cross_street_name VARCHAR(MAX),
    off_street_name VARCHAR(MAX)
);
"""

create_casualty_table = """
CREATE TABLE IF NOT EXISTS casualty_table(
    unique_id INTEGER,
    total_persons_killed INTEGER,
    total_persons_injured INTEGER,
    total_cyclists_killed INTEGER,
    total_cyclists_injured INTEGER,
    total_motorists_injured INTEGER,
    total_motorists_killed INTEGER,
    contributing_factor_vehicle_1 VARCHAR(MAX),
    contributing_factor_vehicle_2 VARCHAR(MAX),
    contributing_factor_vehicle_3 VARCHAR(MAX),
    contributing_factor_vehicle_4 VARCHAR(MAX),
    contributing_factor_vehicle_5 VARCHAR(MAX),
    vehicle_type_code_1 VARCHAR(MAX),
    vehicle_type_code_2 VARCHAR(MAX),
    vehicle_type_code_3 VARCHAR(MAX),
    vehicle_type_code_4 VARCHAR(MAX),
    vehicle_type_code_5 VARCHAR(MAX)
);
"""

crate_collision_staging = """
CREATE TABLE IF NOT EXISTS collision_staging(
    date TIMESTAMP,
    time TIMESTAMP,
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
    vehicle_type_code_1 VARCHAR(MAX),
    vehicle_type_code_2 VARCHAR(MAX),
    vehicle_type_code_3 VARCHAR(MAX),
    vehicle_type_code_4 VARCHAR(MAX),
    vehicle_type_code_5 VARCHAR(MAX)
);
"""