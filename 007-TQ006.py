try:
  n=int(input())
except:
  pass
else:
    if n>1 and n<1001:
      try:
        nums=list(map(int,input().split()))
      except:
        pass
      else:
        if len(nums)==n:
          for num in nums:
            if num<1 or num>10**9:
              quit()
          ch=0
          nch=0
          for i in range(len(nums)):
            if i%2==0:
              if nums[i]%2==0:
                ch+=1
                pch=i+1
            else:
              if nums[i]%2!=0:
                nch+=1
                pnch=i+1
          if ch==1 and nch==1:
            print(pch,pnch)
          else:
            print("-1 -1")