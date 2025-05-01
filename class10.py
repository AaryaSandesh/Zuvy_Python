# Question 1 :position of numbers making sum equal to target and list is sorted
# method 1
# def func(list,target):
#     for i in range (0,len(list)-1):
#         for j in range (i+1,len(list)-2):
#             if list[i]+list[j]==target:
#                 print(i)
#                 print(j)
# list=[2,7,11,15]
# target=9
# func(list,target)
#  TC :O(n2)

# method 2
# i=0
# j=len(list)-1
# while i<j :
#     if list[i]+list[j]==target:
#         print(i+1,j+1)
#         break
#     elif list[i]+list[j]>target:
#         j-=1
#     else:
#         i-=1
# Question 2: Find the number occuring one time only
# li=[1,3,4,5,6,7,1,2,3,4,5,6,7]
# ans=0
# Method 1:
# for num in li:
#     ans^=num
# print(ans)
# method 2:
# for i in range (0,len(li)):
#     count=0
#     for j in range (0,len(li)):
#         if li[i]==li[j]:
#             count+=1
#     if count==1:
#         print(li[i])
# method 3:
# set appoach

# Question 3: valid palindrome
def palin(li):
    i=0
    j=len(li)-1
    while i<j:
        if li[i]==li[j]:
            i+=1
            j-=1
        else:
            return ispalin(li,i+1,j) or  ispalin(li,i,j-1)
         
    return True

def ispalin(li,i,j):
    while i<j:
        if li[i]!=li[j]:
            return False
        i+=1
        j-=1
    return True
        

li="abcda"
ans=palin(li)
print(ans)
     

           
    



 



 