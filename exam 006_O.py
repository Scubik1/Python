try:
  fl=list(map(int,input().split()))
except:
  pass
else:
  if len(fl)==2 and fl[0]>=1 and fl[0]<=2*10**5 and fl[1]>=1 and fl[1]<=5*10**5:
    n=fl[0]
    q=fl[1]
    try:
      ais=list(map(int,input().split()))
    except:
      pass
    else:
      if len(ais)==n:
        for ai in ais:
          if ai<0 or ai>10**9:
            quit()
        outs=list()
        for counter in range(q):
          qi=list(input().split())
          if qi[0]!='?' and qi[0]!='+':
            quit()
          if qi[0]=='?':
            try:
              l=int(qi[1])
              r=int(qi[2])
              k=int(qi[3])
              b=int(qi[4])
            except:
              quit()
            else:
              if len(qi)!=5 or l<1 or l>n or r<1 or r>n or l>r or k<0 or k>10**9 or b<0 or b>10**9:
                quit()
              cutais=ais[l-1:r]
              print(l, r, cutais)
              Max=max(cutais)
              print(Max)
              i=ais.index(Max)+1
              print(i)
              outs.append(min(Max, k*i+b))
          if qi[0]=='+':
            try:
              l=int(qi[1])
              r=int(qi[2])
              x=int(qi[3])
            except:
              quit()
            else:
              if len(qi)!=4 or l<1 or l>n or r<1 or r>n or l>r or x<0 or x>10**9:
                quit()
              for counter in range(l-1,r):
                ais[counter]+=x
              print(ais)
        for out in outs:
          print(out)        