#Task 1: Check if a Number is Even or Odd

a=int(input("enter your number:"))

if a%2==0:
    print(a,"is the even number")
else:
    print(a,"is the odd number")


#Task 2: Sum of Integers from 1 to 50 Using a Loop

t=50
i=1
n=0
while i<=t:
    n=n+i
    i+=1
print("the sum of the number 1 to 50 is :",n)