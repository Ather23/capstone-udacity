from harver_sine import HarverSine
from red_shift_connection import RedShiftConnection


class StationProximityCal:
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
            md5(bikeid || starttime) as bike_trip_id,
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

    bike_trip_query = """
    
    """

    rds = RedShiftConnection()

    def __int__(self, rds_connection):
        super(StationProximityCal, self).__init__()

    def fetch_zip_codes(self):
        """


        :return: list(zip_codes)
        """
        pass

    def fetch_bike_trips_from_staging(self):
        """

        :return: list((),()..())
        """
        pass

    def fact_table_data(self):
        """

        :return: List of trip incidents
        """

        for trip in self.fetch_bike_trips_from_staging():
            print("Trip: " + trip[0])
            longlat = (trip[3], trip[4])
            for colzip in self.fetch_zip_codes():
                z_xy = (colzip[1], colzip[2])
                if HarverSine().is_within_radius(longlat, z_xy):
                    inc = TripIncidentFactTbl()
                    inc.trip_incident_id="'make hash'"
                    inc.trip_id="trip id from bikeshare"
                    inc.unique_id = "unique ids by zip code from collision table"
                    inc.start_station_id = trip[3]
                    inc.end_station_id = trip[7]



class TripIncidentFactTbl:
    trip_incident_id = ""
    trip_id = 0
    unique_id = 0
    start_station_id = 0
    end_station_id = 0

    def __init__(self):
        super(TripIncidentFactTbl, self).__init__()
