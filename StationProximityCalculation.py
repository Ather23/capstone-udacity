from harver_sine import HarverSine
from query_dwh_tables import TableOperations
from red_shift_connection import RedShiftConnection


class ProximityCalculation:
    zip_codes_query = """
        SELECT distinct
            zip_code,
            latitude,
            longitude        
        FROM
            collision_staging        
        WHERE
            latitude IS NOT NULL AND
            longitude IS NOT NULL AND
            zip_code IS NOT NULL AND
            zip_code <> TRIM('');    
    """
    bike_trips_query = """
        SELECT 
            bikeid,
            starttime,
            start_station_id,
            end_station_id,
            start_station_latitude,
            start_station_longitude,
            end_station_latitude,
            end_station_longitude     
        FROM 
        public.bike_share_staging
        
        WHERE
            start_station_latitude IS NOT NULL AND
            start_station_longitude IS NOT NULL
        limit 100;    
    """
    uniqueid_query = """
        SELECT unique_id
        FROM collision_staging
        WHERE zip_code like '{}';    
    """

    rds = RedShiftConnection()

    def __int__(self, rds_connection):
        super(ProximityCalculation, self).__init__()

    def fetch_zip_codes(self):
        """
        Fetchs all zipcodes and long,lat
        from bike sharing staging
        :return: list(zip_codes,lat,long)
        """
        tblop = TableOperations()
        data = tblop.fetch_data(self.zip_codes_query)

        return data

    def fetch_bike_trips_from_staging(self):
        """

        :return: list(
            (
            bike_id,
            start_time,
            start_station_id,
            end_station_id,
            start_station_latitude,
            start_station_longitude,
            end_station_latitude,
            end_station_longitude
            )
        )
        """
        tblop = TableOperations()
        data = tblop.fetch_data(self.bike_trips_query)
        return data

    def get_unique_id_from_zipcode(self, zip_code):
        tblop = TableOperations()
        data = tblop.fetch_data(self.zip_codes_query.format(zip_code))
        return data

    def fact_table_data(self):
        """

        :return: List of trip incidents
        """

        incidents_list = []
        for trip in self.fetch_bike_trips_from_staging():
            print("Trip: " + trip[0])
            longlat = (trip[3], trip[4])
            for colzip in self.fetch_zip_codes():
                z_xy = (colzip[1], colzip[2])
                zipcode = colzip[0]
                if HarverSine().is_within_radius(longlat, z_xy):
                    inc = TripIncidentFactTbl()
                    inc.trip_incident_id = self.generate_hash(
                        trip[0],
                        trip[1].strftime('%Y-%m-%d %H:%M:%S'),
                        trip[2]
                    )
                    inc.start_station_id = trip[3]
                    inc.end_station_id = trip[7]
                    inc.zip_code = zipcode
                    uniqueids = self.get_unique_id_from_zipcode(zipcode)
                    for id in uniqueids:
                        inc.unique_id = id[0]
                        incidents_list.append(inc)

    def generate_hash(self, bike_id, starttime, start_station_id):
        string = str(bike_id) + starttime + str(start_station_id)
        return hash(string)


class TripIncidentFactTbl:
    trip_incident_id = ""
    unique_id = 0
    start_station_id = 0
    end_station_id = 0
    zip_code = ""

    def __init__(self):
        super(TripIncidentFactTbl, self).__init__()
