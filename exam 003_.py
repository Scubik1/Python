try:
  FirstLine=list(map(int,input().split()))
except:
  pass
else:
  if len(FirstLine)==2 and FirstLine[0]>=1 and FirstLine[0]<=10**5 and FirstLine[1]>=1 and FirstLine[1]<=10**9:
    n=FirstLine[0]
    m=FirstLine[1]    
    try:
      ais=list(map(int,input().split()))
    except:
      pass
    else:
      if len(ais)==n:
        for ai in ais:
          if ai<1 or ai>10**9:
            quit()
        maxRest=0
        for mi in range(1,m+1):
          Rest=0
          sumai=0
          for ai in ais:
            if sumai+ai<=mi:
              sumai+=ai
          if mi-sumai>Rest:
            Rest=mi-sumai
          if Rest>maxRest:
            maxRest=Rest
        print(maxRest)        
