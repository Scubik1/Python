try:
  t=int(input())
except:
  pass
else:
  if t>0 and t<1001:
    results=list()
    for i in range(t):
      try:
        n=int(input())
      except:
        quit()
      else:
        if n>0 and n<=10**5:
          try:
            ais=list(map(int,input().split()))
          except:
            quit()
          else:
            if len(ais)==n:
              for ai in ais:
                if ai<1 or ai>10**9:
                  quit()
              cSoc=ais.count(1)
              cNotSoc=0
              for ai in ais:
                if ai>1:
                  if cNotSoc==0:
                    cNotSoc=2
                  cNotSoc=cNotSoc+ai-2
              if cNotSoc>=cSoc or n<=2:
                results.append("Yes")
              else:
                results.append("No")
              #print(cNotSoc, cSoc)
    for result in results:
      print(result)  
