from math import (radians,sin,cos,asin,sqrt)
def haversine(lat1, lon1, lat2, lon2):
  R = 6372.8
  dLat = radians(lat2 - lat1)
  dLon =radians(lon2 - lon1)
  lat1 = radians(lat1)
  lat2 = radians(lat2)
  a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
  c = 2*asin(sqrt(a))
  return R * c

class Tracker:
    def __init__(self):
        self.info = {}
    def addPosition(self, object_name, latitude, longitude):
        path = self.info.setdefault(object_name,[])
        path.append((latitude,longitude))
        # [object_name] = 
    def printPath(self, object_name):
        for (lat,long) in self.info.get(object_name,[]):
            print(lat,long)
    def pathLength(self,object_name):
        path = self.info.get(object_name,[])
        total = 0
        if len(path) > 1:
            prev = path[0]
            for cur in path[1:]:
                (lat1,lon1) = prev
                (lat2,lon2) = cur
                total += haversine(lat1, lon1, lat2, lon2)
                prev = cur
        return total
