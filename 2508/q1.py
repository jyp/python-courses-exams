
import math
def ci(mean,z,s,n):
  if n > 0:
     dx = z*s/math.sqrt(n)
     print("interval:", [mean-dx, mean+dx])
  else:
     print("Error: empty sample")

ci(100,1.96,10,5)
ci(100,1.645,10,0)
