# Question 1
# Remove Element
nums = [3,2,2,3]
val=3

sp=0
ep=len(nums)-1
while sp<=ep :
   while ep>=0 and nums[ep]==val :
     ep=ep-1
   if sp<=ep and nums[sp]==val :
      nums[sp]=nums[ep]
      ep=ep-1
     
   sp=sp+1

print(ep + 1) 
    
