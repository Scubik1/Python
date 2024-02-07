def perebor(List, num):
  OutList=[]
  if num==-1:
    return(OutList)
  for iList in List[num]:
    print(iList)
    perebor(List, num-1)
  

# def f(x):
#     if x==0:
#         return 0
#     for i in range(2):
#         print(x)
#         f(x-1)
# print(f(3))



import re
try:
  fl=list(map(int,input().split()))
except:
  pass
else:
  if len(fl)==2 and fl[0]>=1 and fl[0]<=3*10**5 and fl[1]>=1 and fl[1]<=30:
    n=fl[0]
    k=fl[1]
    ks=list()
    for counter in range(k):
      ks.append(input())
      if len(ks[counter])>10 or re.search(r'[^a-z]', ks[counter]):
        quit()
    pis=[]
    ais=[]
    cis=[]
    for i in range(n):
      vs=list(input().split())
      try:
        pis.append(int(vs[0]))
        ais.append(int(vs[1]))
      except:
        quit()
      else:
        cis.append(vs[2])
        if len(vs)!=3 or pis[i]<0 or pis[i]>n or ais[i]<0 or ais[i]>10**4 or len(cis[i])>10 or re.search(r'[^a-z]', cis[i]):
          quit()
    trs=[]
    for i in range(n):
      if pis[i]==0:
        root=i+1
      if pis[i]==1:
        trs.append([root,i+1])
      if pis[i]>1:
        for tr in trs:
          if tr[-1]==pis[i]:
            tr.append(i+1)
    print(trs)
    ctrs=[]
    for i in range(len(trs)):
      ctrs.append(0)
      for j in range(len(trs[i])):
        ctrs[i]+=ais[trs[i][j]-1]
    print(ctrs)
    ktrs=[]
    for ki in ks:
      ktrs.append([])
      for i in range(len(trs)):
        for j in range(len(trs[i])):
          if cis[trs[i][j]-1]==ki:
            ktrs[ks.index(ki)].append(i)
            break
    print(ktrs)
    sums=[]
    for i in ktrs[0]:
          for i1 in ktrs[1]:  
            for i2 in ktrs[2]:  
              ltrs=[]
              ltrs=list(set([i,i1,i2]))
                #print(i,i1,i2)
                #print(ltrs)
              summ=0
              for ltr in ltrs:
                summ+=ctrs[ltr]
              sums.append(summ)
    print(min(sums))
    ltrs=[]
    ltrs=perebor(ktrs,k-1)
 
        
    
    
    

