try:
  inp=list(map(int,input().split()))
except:
  pass
else:
  if len(inp)==2 and inp[0]>1 and inp[0]<101 and inp[1]>1 and inp[1]<101:
    cCow=inp[0]
    TimeExit=inp[1]
    try:
      Floor=list(map(int,input().split()))
    except:
      pass
    else:
      if len(Floor)==cCow:
        for i in range(cCow):
          if Floor[i]>100 or (i!=0 and Floor[i-1]>Floor[i]):
            quit()
        try:
          FloorExit=int(input())
        except:
          pass
        else:
          if FloorExit>0 and FloorExit<=cCow:
            if TimeExit>=Floor[FloorExit-1]-Floor[0] or TimeExit>=Floor[cCow-1]-Floor[FloorExit-1]:
              print(Floor[cCow-1]-Floor[0])
            else:
              if Floor[FloorExit-1]-Floor[0]<Floor[cCow-1]-Floor[FloorExit-1]:
                print(Floor[FloorExit-1]+Floor[cCow-1]-2*Floor[0])
              else:
                print(2*Floor[cCow-1]-Floor[FloorExit-1]-Floor[0])