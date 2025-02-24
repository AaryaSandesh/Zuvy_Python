# nested lists : 2d array
matrix=[
    [1,3,4], #in one list we are having 3 different lists
    [5,7,8],
    [8,9,0]
]
print(matrix)

print(matrix[1][0])

# Question 1
# Sum of all numbers :
b=int(input("Size of list:"))
li=[]
for i in range (b) :
    c=int(input("Enter number:"))
    li.append(c)

sum=0
for i in li:
    sum=sum+i
print(sum)

# Avg of List
avg=sum/b
print(avg)

h=int(input("Size of list:"))
list=[]
for i in range (h) :
    m=int(input("Enter number:"))
    list.append(m)
target=int(input("Enter target:"))

flag=-1
for i in range(len(list)) :
    if list[i]==target :
         flag=i
         break
    
print(flag)