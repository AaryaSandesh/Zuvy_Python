a=5#integer to string
n=str(a)
print(n)
print(type(n))

b="5"# if written "a" : it is not number so error
n1=int(b)
print(b)
print(type(n1))

#user input : to make the program dynamic 
val=input("Enter your value: ")
print(val)
print(type(val))# always taken as str format only

# Activity 1: converting default str to float
count=input("Enter the number :")
co=float(count)
print(co)
print(type(co))

p=float(input("Enter p:"))
r=float(input("Enter r:"))
t=float(input("Enter t:"))
SI=float(p*r*t)/100
print(SI)

v1=int(input("Enter v1:"))
if v1%2==0 :
    print("even")
else :
    print("odd")

temp=float(input("Enter temperature :"))
fah=float(((9*temp)/5)+32)
print(fah)


