# Tupple and Functions
# Lists are mutable
# Tupples are immutable
# indexing is same as list
# can include any data type in tupple and list
tup=(1,2,3,4,5,6)
lst=[2,3,4,4,5,6]
# print(type(tup))
# print(type(lst))
# lst[2]=40000
# print(lst)

# print(tup[0])
# tup[0]=3333
# print(tup) gives error
# cannot be extended and appended
# cannot remove any element
# print(tup[-1])  #they will start from backward direction
# print(tup[-2])
# print(tup[-3])
for i in tup :
    print(i)

# concatination of two tupples
tpl1=(2,2)
tpl2=(3,3)
print(tpl1+tpl2) #creating a new tupple for their combination and it becomes immutable
print(tpl1)
print(tpl2)

# Nested tupples
tp1=(8,3,3,4,5,6)
tp2=(3,4,5,6,7)
tp3=(tp1+tp2)
print(tp3)

# created my own tupple
t=('python',)*5
print(t)


# Slicing in tupple (taking small portion)
tupp=(1,2,3,3,4,4,5,5,5,5,6)
t3=tupp[1:] 
t4=tupp[0:5] #doesnot take last index
t5=tupp[1:-6] #go till -6 index from back where that index is exclusive
t6=tupp[-6 : -1]
print(t3)
print(t4)
print(t6)

t7=tupp[::-1]
# print reverse


# deletion from tupple
# del tup
# print(tup) #gives error as we have deleted that and then we r printing that
# we cannot delete a single element
print(len(tupp))
# heterogenous
tupple=("single","akhil",2,2,2,2,3) 