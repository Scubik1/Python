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
    #print(trs)
    ctrs=[]
    for i in range(len(trs)):
      ctrs.append(0)
      for j in range(len(trs[i])):
        ctrs[i]+=ais[trs[i][j]-1]
    #print(ctrs)
    ktrs=[]
    for ki in ks:
      ktrs.append([])
      for i in range(len(trs)):
        for j in range(len(trs[i])):
          if cis[trs[i][j]-1]==ki:
            ktrs[ks.index(ki)].append(i)
            break
    #print(ktrs)
    sums=[]
    ltrs=[]
    match k:
      case 1:
        for i in ktrs[0]:
          ltrs=list(set([i]))
          summ=0
          for ltr in ltrs:
            summ+=ctrs[ltr]
          sums.append(summ)        
      case 2:
        for i in ktrs[0]:
          for i1 in ktrs[1]:  
            ltrs=list(set([i,i1]))
            summ=0
            for ltr in ltrs:
              summ+=ctrs[ltr]
            sums.append(summ)
      case 3:
        for i in ktrs[0]:
          for i1 in ktrs[1]:  
            for i2 in ktrs[2]:  
              ltrs=list(set([i,i1,i2]))
              summ=0
              for ltr in ltrs:
                summ+=ctrs[ltr]
              sums.append(summ)
      case 4:
        for i in ktrs[0]:
          for i1 in ktrs[1]:  
            for i2 in ktrs[2]:
              for i3 in ktrs[3]:  
                ltrs=list(set([i,i1,i2,i3]))
                summ=0
                for ltr in ltrs:
                  summ+=ctrs[ltr]
                sums.append(summ)
      case 5:
        for i in ktrs[0]:
          for i1 in ktrs[1]:  
            for i2 in ktrs[2]:
              for i3 in ktrs[3]:
                for i4 in ktrs[4]:
                  ltrs=list(set([i,i1,i2,i3,i4]))
                  summ=0
                  for ltr in ltrs:
                    summ+=ctrs[ltr]
                  sums.append(summ)
      case 6:
        for i in ktrs[0]:
          for i1 in ktrs[1]:  
            for i2 in ktrs[2]:
              for i3 in ktrs[3]:
                for i4 in ktrs[4]:
                  for i5 in ktrs[5]:
                    ltrs=list(set([i,i1,i2,i3,i4,i5]))
                    summ=0
                    for ltr in ltrs:
                      summ+=ctrs[ltr]
                    sums.append(summ)
      case 7:
        for i in ktrs[0]:
          for i1 in ktrs[1]:  
            for i2 in ktrs[2]:
              for i3 in ktrs[3]:
                for i4 in ktrs[4]:
                  for i5 in ktrs[5]:
                    for i6 in ktrs[6]:
                      ltrs=list(set([i,i1,i2,i3,i4,i5,i6]))
                      summ=0
                      for ltr in ltrs:
                        summ+=ctrs[ltr]
      case 8:
        for i in ktrs[0]:
          for i1 in ktrs[1]:  
            for i2 in ktrs[2]:
              for i3 in ktrs[3]:
                for i4 in ktrs[4]:
                  for i5 in ktrs[5]:
                    for i6 in ktrs[6]:
                      for i7 in ktrs[7]:
                        ltrs=list(set([i,i1,i2,i3,i4,i5,i6,i7]))
                        summ=0
                        for ltr in ltrs:
                          summ+=ctrs[ltr]
                        sums.append(summ)
      case 9:
        for i in ktrs[0]:
          for i1 in ktrs[1]:  
            for i2 in ktrs[2]:
              for i3 in ktrs[3]:
                for i4 in ktrs[4]:
                  for i5 in ktrs[5]:
                    for i6 in ktrs[6]:
                      for i7 in ktrs[7]:
                        for i8 in ktrs[8]:
                          ltrs=list(set([i,i1,i2,i3,i4,i5,i6,i7,i8]))
                          summ=0
                          for ltr in ltrs:
                            summ+=ctrs[ltr]
                          sums.append(summ)
      case 10:
        for i in ktrs[0]:
          for i1 in ktrs[1]:  
            for i2 in ktrs[2]:
              for i3 in ktrs[3]:
                for i4 in ktrs[4]:
                  for i5 in ktrs[5]:
                    for i6 in ktrs[6]:
                      for i7 in ktrs[7]:
                        for i8 in ktrs[8]:
                          for i9 in ktrs[9]:
                            ltrs=list(set([i,i1,i2,i3,i4,i5,i6,i7,i8,i9]))
                            summ=0
                            for ltr in ltrs:
                              summ+=ctrs[ltr]
                            sums.append(summ)
      case 11:
        for i in ktrs[0]:
          for i1 in ktrs[1]:  
            for i2 in ktrs[2]:
              for i3 in ktrs[3]:
                for i4 in ktrs[4]:
                  for i5 in ktrs[5]:
                    for i6 in ktrs[6]:
                      for i7 in ktrs[7]:
                        for i8 in ktrs[8]:
                          for i9 in ktrs[9]:
                            for i10 in ktrs[10]:
                              ltrs=list(set([i,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10]))
                              summ=0
                              for ltr in ltrs:
                                summ+=ctrs[ltr]
                              sums.append(summ)
      case 12:
        for i in ktrs[0]:
          for i1 in ktrs[1]:  
            for i2 in ktrs[2]:
              for i3 in ktrs[3]:
                for i4 in ktrs[4]:
                  for i5 in ktrs[5]:
                    for i6 in ktrs[6]:
                      for i7 in ktrs[7]:
                        for i8 in ktrs[8]:
                          for i9 in ktrs[9]:
                            for i10 in ktrs[10]:
                              for i11 in ktrs[11]:
                                ltrs=list(set([i,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11]))
                                summ=0
                                for ltr in ltrs:
                                  summ+=ctrs[ltr]
                                sums.append(summ)
      case 13:
        for i in ktrs[0]:
          for i1 in ktrs[1]:  
            for i2 in ktrs[2]:
              for i3 in ktrs[3]:
                for i4 in ktrs[4]:
                  for i5 in ktrs[5]:
                    for i6 in ktrs[6]:
                      for i7 in ktrs[7]:
                        for i8 in ktrs[8]:
                          for i9 in ktrs[9]:
                            for i10 in ktrs[10]:
                              for i11 in ktrs[11]:
                                for i12 in ktrs[12]:
                                            ltrs=list(set([i,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12]))
                                            summ=0
                                            for ltr in ltrs:
                                              summ+=ctrs[ltr]
                                            sums.append(summ)
      case 14:
       for i in ktrs[0]:
        for i1 in ktrs[1]:  
         for i2 in ktrs[2]:
          for i3 in ktrs[3]:
           for i4 in ktrs[4]:
            for i5 in ktrs[5]:
             for i6 in ktrs[6]:
              for i7 in ktrs[7]:
               for i8 in ktrs[8]:
                for i9 in ktrs[9]:
                 for i10 in ktrs[10]:
                  for i11 in ktrs[11]:
                   for i12 in ktrs[12]:
                    for i13 in ktrs[13]:
                                     ltrs=list(set([i,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13]))
                                     summ=0
                                     for ltr in ltrs:
                                       summ+=ctrs[ltr]
                                     sums.append(summ)
      case 15:
       for i in ktrs[0]:
        for i1 in ktrs[1]:  
         for i2 in ktrs[2]:
          for i3 in ktrs[3]:
           for i4 in ktrs[4]:
            for i5 in ktrs[5]:
             for i6 in ktrs[6]:
              for i7 in ktrs[7]:
               for i8 in ktrs[8]:
                for i9 in ktrs[9]:
                 for i10 in ktrs[10]:
                  for i11 in ktrs[11]:
                   for i12 in ktrs[12]:
                    for i13 in ktrs[13]:
                     for i14 in ktrs[14]:
                                     ltrs=list(set([i,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14]))
                                     summ=0
                                     for ltr in ltrs:
                                       summ+=ctrs[ltr]
                                     sums.append(summ)
    print(min(sums))

 
        
    
    
    

