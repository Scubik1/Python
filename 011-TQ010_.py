def square(lx,ly):
  square=0
  tlx=lx[:]
  tly=ly[:]
  tlx.append(tlx[0])
  tlx.reverse()
  tly.append(tly[0])
  tly.reverse()
  for i in range(len(tlx)-1):
    square+=tlx[i]*tly[i+1]-tly[i]*tlx[i+1]
#   if square>=0:
  return(abs(square/2))
#   else: 
#     tlx.reverse()
#     tly.reverse()
#   for i in range(len(tlx)-1):
#     square+=tlx[i]*tly[i+1]-tly[i]*tlx[i+1]
#   return(square/2)
     
def halfCoordinates(xlist,x):
  halfxlist=xlist[:]
  for i in range(len(halfxlist)):
    if halfxlist[i]>x:
      halfxlist[i]=x
  return(halfxlist)
  
try:
  n=int(input())
except:
  pass
else:
  if n>0 and n<1001:
    lx=list()
    ly=list()
    for i in range(n):
      try:
        nums=list(map(int,input().split()))
      except:
        quit()
      else:
        if len(nums)==2 and nums[0]>=-1000 and nums[0]<=1000 and nums[1]>=-1000 and nums[1]<=1000:
          lx.append(nums[0])
          ly.append(nums[1])
        else:
          quit()
    s=square(lx,ly)
    print(s)
    ltx=lx[:]
    ltx.sort()
    if len(ltx)==1:
      x=ltx[0]
    else:
      x=(ltx[len(ltx)-1]-ltx[0])/2
    hlx=halfCoordinates(lx,x)
    hs=square(hlx,ly)
    dx=0.1
    accuracy=0.0000001
    if hs>s/2+accuracy or hs<s/2-accuracy:
      if hs>s/2:
        ifBigger=True
      else:
        ifBigger=False
      while hs>s/2+accuracy or hs<s/2-accuracy:
        if hs>s/2+accuracy:
          if ifBigger!=True:
            dx=dx/2            
          x=x-dx
          ifBigger=True
        if hs<s/2-accuracy:
          if ifBigger:
            dx=dx/2            
          x=x+dx
          ifBigger=False
        hlx=halfCoordinates(lx,x)
        hs=square(hlx,ly)
    print("%.9f" % x)