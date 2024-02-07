try:
  inp=list(map(int,input().split()))
except:
  pass
else:
  if len(inp)==2:
    l=inp[0]
    r=inp[1]
    if l>0 and r>0 and l<=10**18 and r<=10**18:
      t=l
      count=int()
      str=str(t)
      if len(str)==1:
        while t<=9 and t<=r:
          t+=1
          count+=1
      if t>=r:
        print(count)
      else:
        for i in range(len(str)-1):
          if str[i+1]>str: 


