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
        sumais=sum(ais)
        if sumais<m:
          maxRest=m-sumais
        else:  
          maxRest=0
        # maxai=0
        # for i in range(len(ais-1),len(ais),-1):
        #   if ais[i]>maxai:
        #     maxai=ais[i]
        #     imaxai=i
        for mi in range(1,sumais):
          Rest=0
          sumai=0
          #tls=[mi]#
          for ai in ais:
            if sumai+ai<=mi:
              sumai+=ai
          #    tls.append(ai)#
          if mi-sumai>Rest:
            Rest=mi-sumai
          if Rest>maxRest:
            maxRest=Rest
         #   maxtls=tls[:]#
        print(maxRest)
        #print(maxtls)#
        
