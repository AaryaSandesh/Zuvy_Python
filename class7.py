# Practice Question
# Find the largest element from the list
numbers=[0,4,20,3,8]
largest=float('-inf')
for val in numbers :
    if  largest < val :
       largest= val
print(largest)

#Question2 
list=[10,5,9,8,7,2,-1,8]
target=-1
 
ansli=[]
for i in range (0,len(list)) :
     if target==list[i] :
        ansli.append(i)
if len(ansli) ==0 :
   print(-1)
else :
   print(ansli)

# Question 3
# Two sum from leetcode
# Remove duplicates