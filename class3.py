#increment and decrement operators
a=10
# b=20
# print(a++);//wrong thing
a+=1
print(a)
# b-=1
# print(b)
# no concept of increment decrement operators ++ or --
# Assignment Operator +=,-=,*=,/=,%=,**=
x=5
x+=3
# print(x+=5) : wrong
print(x)
y=8
y/=2
print(y)
#Type Casting :converting one data type into another
 
# int : 4 byte, float : 8 byte, bool : 4 byte, str : depends on the no. of characters(1 char=1 byte)
#implicit  type conversion :
v=7#python done this internally : changed this to float 
print(type(a))
b=3.0
print(type(b))
c=v+b
print(type(c))

d=v*b
print(d)
print(type(d))

#explicit type conversion : user forcefully changing one datatype to another one
# h=5
# n=float(h)
# print(n)
# print(type(n))

n=5.0
h=int(n)
print(h)
print(type(h))



