# Question1
# Get the smallest number from the list
# num=[1,2,3,3,4,88,76]
# smallest=float('inf')
# for i in num :
#     if i< smallest :
#         smallest=i
# print(smallest)

# Question2
# Remove Duplicates from the list
# a=[1,2,3,3,4,5,5,4,3,3,3,3,3]
# a=list(set(a))
# print(a)

#Question3
#Remove the even numbers from the list
# a=[1,2,3,3,4,5,5,4,3,3,3,3,3]
# for i in a :
#     if a[i]%2==0 :
#         del a[i]
#     else :
#         i=i+1
# print(a)

#Question4
# Find the second largest number in the list
# num=[1,2,3,3,4,88,76]
# largest=float('-inf')
# seco_largest=float('-inf')
# for i in num :
#     if i> largest :
#          largest=i


# for i in num :
#      if i>seco_largest and i<largest :
#           seco_largest=i
# print(seco_largest)

#Question5
# Check if all the numbers are prime
# def is_prime(n):
#     if n<2 :
#         return False
#     for i in range (2,int(n**0.5)+1):
#         if n%i==0 :
#             return False
#     return True 
# num=[1,2,3,3,4,88,76]
# all_prime=all(is_prime(i)for i in num)
# print(all_prime)


# Question 6
# Count frequency of list elements
def freq(n,num) :
    count=0
    for i in num :
        if i==n :
            count=count+1
    return count 
num=[1,2,3,3,4,88,76]
nums=[]
for i in num:
 ans=freq(i,num)
 nums.append(ans)

print(nums)