from sys import argv
fnamein=argv[1]
with open(fnamein,'r') as finp:
  try:
    line1=list(map(int,finp.readline().split()))
  except:
    pass
  else:
    if len(line1)==2:
      n=line1[0]
      k=line1[1]
      if n>0 and k>0 and n<1001 and k<10001:
        try:
          nums=list(map(int,finp.readline().split()))
        except:
          pass
        else:
          if len(nums)==n:
            list=list()
            for num in nums:
              if num<1 or num>1000000000:
                quit()
              snum=str(num)
              for i in range(len(snum)):
                if snum[i]=='9':
                  if i==len(snum)-1:
                    list.append(0)
                else:
                  list.append((9-int(snum[i]))*10**(len(snum)-i-1))
                  break
            list.sort(reverse=1)
            sum=int()
            if k>len(list):
              c=len(list)
            else:
              c=k
            for i in range(c):
              sum+=list[i]
            fnameout=argv[2]
            with open(fnameout,'w') as fout:
              fout.write(str(sum))

                        
       