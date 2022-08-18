#!/usr/bin/env python3

def check(n):
    if (n < 2):
        return (n % 2 == 0)
    return (check(n - 2))
n=int(input("Enter number:"))
if(check(n)==True):
      print("Number is even!")
else:
      print("Number is odd!")

if(n>0):
    print("Number is positive")
else:
    print("Number is negative")

temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)
