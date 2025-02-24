#questions
number=int(input("Enter the number:"))
n=number%10
if(n%3==0):
    print("true")
else :
    print("false")

#2
year=int(input("Enter the year :"))
if(year%400==0) :
    print("the year is leaf year")
elif(year%100==0) :
    print("The year is not a leap year.")
elif (year%4==0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

#3
number=int(input("Enter a number:"))
if(number>=1 and number<=12) :
    match number :
        case 1:
            if(number==1) :
                print("January")
        case 2:
            if(number==2) :
                print("February")
         #continues till december
         
else :
    print("invalid")

#4
num=int(input("Enter the number1:"))
num1=int(input("Enter the number2:"))
num2=int(input("Enter the number3:"))
if(num>=num1 and num>=num2):
    print(num)
elif(num1>=num and num1>=num2):
    print(num1)
else:
    print(num2)

#5
length=int(input("Enter the kilometer:"))
if(length<=10) :
    print(11*length)
elif(length>=11 and length<=100) :
    print(10*11+(length-10)*10)
else :
    print(10*11+90*10+(length-100)*9)

#6
days=int(input("Enter the no. of days:"))
if(days<=5) :
    print(2*days)
elif(days>=6 and days<=10) :
    print( 10+(days-5)*3)
elif(days>=11 and days<=15) :
    print(40+(days-10)*4)
else :
    print(100+(days-15)*5)