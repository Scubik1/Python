nums=[0,0]
for i in range(2):
  try:
    nums[i]=int(input())
  except:
    quit()
  else:
    if nums[i]<-32000 or nums[i]>32000:
      quit()
print(nums[0]+nums[1])