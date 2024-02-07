try:
  fl=list(map(int,input().split()))
except:
  pass
else:
  if len(fl)==3 and fl[0]>=1 and fl[0]<=10**5 and fl[1]>=0 and fl[1]<=10**5 and fl[2]>=1 and fl[2]<=3*10**5:
    n=fl[0]
    m=fl[1]
    q=fl[2]    
    try:
      ais=list(map(int,input().split()))
    except:
      pass
    else:
      if len(ais)==n:
        relations=list()
        for ai in ais:
          if ai<0 or ai>10**9:
            quit()
          relations.append(list())
        for i in range(m):
          try:
            mi=list(map(int,input().split()))
          except:
            quit()
          else:
            if len(mi)!=2 or mi[0]<1 or mi[0]>10**5 or mi[1]<1 or mi[1]>10**5:
              quit()
          relations[mi[0]-1].append(mi[1])
          relations[mi[1]-1].append(mi[0]) 
        outs=list()
        for i in range(q):
          qi=list(input().split())
          if qi[0]!='?' and qi[0]!='+':
            quit()
          if qi[0]=='?':
            try:
              v=int(qi[1])
            except:
              quit()
            else:
              if len(qi)!=2 or v<1 or v>n:
                quit()
              outs.append(ais[v-1])
          if qi[0]=='+':
            try:
              v=int(qi[1])
              x=int(qi[2])
            except:
              quit()
            else:
              if len(qi)!=3 or v<1 or v>n or x<0 or x>10**4:
                quit()
              #print(ais)
              for relation in relations[v-1]:
                ais[relation-1]+=x
              #print(ais)
        for out in outs:
          print(out)
            