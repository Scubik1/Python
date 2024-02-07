import math
try:
  parts = int(input())
except:
  pass
else:
  if parts>0 and parts<=2000000000:
    print(math.ceil(math.log(parts,2)))