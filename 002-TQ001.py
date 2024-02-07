try:
  num=list(map(int,input().split()))
except:
  pass
else:
  if len(num)==4:
    for inum in num:
      if inum<1 or inum>100:
        quit()
    if num[3]<=num[1]:
      res=num[0]
    else:
      res=num[0]+(num[3]-num[1])*num[2]
    print(res)
