# Array is called List in Python
# no any kind of restriction for same data type .It can have mixed data types
# dont need to specify the size as well
# a=[10,"aarya",30.66,True]
# print(a)

b=["apple","banana","orange"]
print(b)

# method 2 --to create list
d=list[(10,20,30,40,50)] #function
print(d)

# we can create a list with the repeating elements as well!!
e=[2]*5 # instead of 2 we can use any data structure here
print(e)

# Accessing the elements
# index start from 0
print(b[0]) #starts from first
print(b[-1]) # This will print the elements from backward and the last element will have the index of -1

# Adding the element
# append,extend,insert : 3 functionalities
# Append :Adds the elemnts at the end of the list
b.append("custardapple")
print(b)

# Insert will add the element at specific index
b.insert(0,"guava") # elements gets shifted and not deleted
print(b)

# when we want to add more than one elements.The elemnts are added at the end of list
b.extend([1,2,3,4]) # it is actually taking another list.This list is then added at the end
print(b)



# Update
v=[1,2,3,4,5,6,7,8,9,1,2,3,4,4,5,5,6]
v[3]=66666
print(v)


# Remove
# remove,pop,del

# Remove : removes the first occurance of the value that you have passed.Other occurances remain same
v.remove(1)
print(v)

# pop :remove the element from the specific index and if index not specified removes the index from last
removed=v.pop()
print(v)

rem=v.pop(2)
print(v)

# delete :directly specify the element that we wanna delete
del v[10]
print(v)
# pop is a function and delete is a property

