# python does not support do while loop
# two types: for,while
# for loops are used for iterating lists,strings,dictionaries
languages=['Swift','go','java','python'] 
# this above one is list
# access elements one by one
for i in languages :
    print(i)
# iteratable :where we want to travel --languages
language="Javascript"
for lang in language :
    print(lang)
    print("------------")

print("End of the loop")  #not in the scope of for loop as not written with tab space

 
for i in range (-10,10) : 
    print(i)
# 10 is exclueded

# break and continue
for i in range (0,4) :
  if i ==2 :
     break
  print(i)


for i in range (0,4) :
  if i ==2 :
      continue
  print(i)

  for i in range (0,10) :
     if(i==2 or i==6 or i==9) :
        print(i)

# nested loops
for i in range (0,2) :
   for j in range(0,2) :
      print(i,j)
print("------------")


# while loop
number=1
while number<= 4:
   print(number)
   number=number+1

num=int(input("Enter the number :"))
while(num!=0) :
   print(num)
   num=int(input("Enter the number :"))

print("You have entered zero")
# for loop : when we know the exact no. of iterations
# while loop :when we dont know the num. of iterations

num1=int(input("Enter the number :"))
while(num1!=0) :
   while(num1%2==0) :
      print(num1)
      num1=num1-1
num=num/10
    