#Conditionals
# print("Conditionals")
#ex : accept cookies or reject cookies while visiting a website
age=10
# if age>= 18 : print("eligible")
# if age>=18 :
#     print("eligible")
if (age>=12) :
    print("travel for free")
else :
    print("pay")



#elif : else if
age=20
if (age<=12) :
    print("u r child")
elif (age<=19) :
    print("u r a teenager")
else :
    print("u r old")


#nested if-else
age1=20
is_member=True#convert to ternary?
if(age1>=60) :
    if is_member :
        print("30% discount")
    else :
        print("20% discount")
else :
    print("you are not eligible")


#Ternary Operator
h=20
s="Adult" if h>=18 else "Minor"
print(s)

#Match Case
number=2
match number :
    case 1:
        print("one")
    case 2:
        print("two")
    case 3 | 4:
        print("combine")
    case _:
        print("other")