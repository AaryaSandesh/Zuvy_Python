# Functions
# def functionname (parameter) :
# return expression
# code readibility and reusuability
def sum(a,b): #function declaration
    print(a+b)

sum(4,5)#function call
# parameters are the vaiables present inside the function declaration parathesis
# arguements are the variables present in the function call paranthesis

# Question 1
# Check prime using function
def checkprime(n):
    count=0
    for i in range (1,n):
        if n%i==0:
            count=count+1
    if count>2:
        print("not prime no.")
    else :
        print("prime")

checkprime(5)

# amstrong number :sum of cubes of its digit
def amst(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit**3
        n=n//10
    return sum

ans=amst(123)
print(ans)


