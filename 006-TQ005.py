try:
  inp=list(map(int,input().split()))
except:
  pass
else:
  if len(inp)==2:
    l=inp[0]
    r=inp[1]
    if l>0 and r>0 and l<=10**18 and r<=10**18:
      ls=list()
      for i in range(1,19):
        for j in range(1,10):
          st=''
          for s in range(1,i+1):
            st+=str(j)
          ls.append(int(st))
      count=0
      for ils in ls:
        if ils>=l and ils<=r:
          count+=1
      print(count)