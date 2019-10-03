import math


class HarverSine:
    """
    HarverSine function to calculate
    harversine distance in km
    """

    def __init__(self):
        pass

    def hav(self, phi):
        return 0.5 * (1 - math.cos(phi))

    def haversine_distance(self, longlat1: tuple, longlat2: tuple):
        """
        Calculates harversine distances in KM
        """
        r = 6371
        lg1, lat1 = (math.radians(longlat1[0]),
                     math.radians(longlat1[1]))
        lg2, lat2 = (math.radians(longlat2[0]),
                     math.radians(longlat2[1]))

        d = self.hav(lat2 - lat1) + math.cos(lat1) * math.cos(lat2) * self.hav(lg2 - lg1)
        d = 2 * r * math.sqrt(math.asin(d))
        return d
