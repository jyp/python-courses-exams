import math

class Kepler():
    # 0 points
    def __init__(self):
        self.observations = {}
    # 5 points
    def observe(self, planet_name, position, time):                                
        planet_obs = self.observations.setdefault(planet_name,[])
        planet_obs.append((position,time))
    # 10 points
    def get_period(self,planet_name):
        planet_obs = self.observations.get(planet_name, [])
        if len(planet_obs) < 2:  # 2 points for the test
            return None
        else:
            ts = []
            for i in range(len(planet_obs) - 1): # 
                (a1,t1) = planet_obs[i]
                (a2,t2) = planet_obs[i+1]
                a = a2-a1
                ts.append(2*math.pi*(t2-t1)/a)
            return sum(ts) / len(ts)
    # 5 points 
    def get_radius(self,planet_name):
        t = self.get_period(planet_name)
        if not t: return None  # 2 points for the test
        return (t**2 * G * M / (4 * math.pi ** 2)) ** (1/3) # 3 points for the formula
    # 5 points (for doing the loop nicely)
    def print_planets(self):
        for p in self.observations:
            print(p, self.get_period(p), self.get_radius(p))

M = 1.991e30
G = 6.67e-11
k = Kepler()

k.observe("earth", 0, 0)
k.observe("earth", 2*math.pi, 31548499)
k.observe("x1", 0, 0)
k.observe("x1", 1, 100)
k.observe("x1", 2, 150)
print(k.get_period("x1"))
print(k.get_radius("x1"))
k.print_planets()
