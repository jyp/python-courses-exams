import math

M = 1.991e30
G = 6.67e-11
radii = {
    "mercury": 57.9e9,
    "venus": 108.2e9,
    "earth": 149.6e9,
    "mars": 228e9,
    "jupiter": 779.3e9,
    "saturn": 1427e9,
    "uranus": 2871e9,
    "neptune": 4497e9,
    "pluto": 5913e9
}

def kepler(R):
    return math.sqrt  ((4* math.pi**2 /(G*M)) * R**3)

# test:
# seconds_per_day = 24*60*60
# print(kepler(radii["earth"]))
def planet_period(name):
  if name in radii:
      print(kepler(radii[name]))
  else:
      print("Unknown planet")
