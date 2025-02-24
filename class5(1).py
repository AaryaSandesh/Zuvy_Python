n=10
if n<20 :
    # print("Hii") i want to do this in future
    pass
# for now i am passing the condition . i want to execute this in future and not right now

for i in range (0,10):
    pass

for i in range (1,11) :
    print(19*i)

# knowing the number is prime or not
num=int(input("Enter a number:"));
count=0
for i in range(1,num):
    if num%i==0:
        count=count+1

if count>2 :
    print("not prime")
else:
    print("prime")