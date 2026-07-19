"""
/* p = float(input("Enter the principal amount: \n"))
n = float(input("Enter the net amount: \n"))
r = float(input("Enter the rate of interest: \n"))

simple_interest = p*n*r

print("Simple interest:\n", simple_interest)
"""


#radius of circle

"""r = int(input("Enter the area for circle"))

x = 3.14 * r * r

print("Area of circle is: \n", x)"""

#average of the three number

"""num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
num3 = float(input("Enter the third number"))

average = num1 + num2 + num3/3

print("Average of the three number", average)"""

#value greater than 2000

"""a = float(input("Enter the number"))

if(a>2000):

    print("value greagter than 2000")

else:

    print("value lesser than 2000")"""

#program to find even odd

"""a = float(input("Enter the number"))

if(a%2==0):
    print("the number is even")
else:
    print("the given number is odd")"""

#program to find positive negative number

"""a = int(input("Enter the number"))

if a>0:
    print("the number is positive")

else:
    print("the number is negative")"""

# program to find if age is vaid for voting

"""age = float(input("Enter the age"))

if age>=18:
    print("the age is valid for voting")
else:
    print("the age is not valid for voting")"""

#program to find incentive in salary

"""x = float(input("enter the salary"))
if x>=40000:
    print("incentive 10 percent",x*10/100)
else:
    print("salary should be greater than 400000")"""


#Total marks greater than 500 grade 'a' else work hard:

"""x = float(input("enter the current marks"))
if x>500:
    print("the current marks is greater than 500")
else:
    print("the current marks is less than 500")"""

#Valid ATM Pin program

"""a = float(input("Enter the 4 digit number"))

if a>=1000 and a<=9999:
    print("The entered number is valid")
else:
    print("Pin is not valid")"""

#elif example
"""
a = float(input("Enter the number"))

if a==10:
    print("A = ", a)

elif a==20:
    print("A = ", a)
elif a==30:
    print("A = ", a)
elif a==40:
    print("A = ", a)
else:
    print("invalid")"""

#program to find which is largest number:
"""
a = float(input("Enter the number"))
b = float(input("Enter the number"))
c = float(input("Enter the number"))

if a>b and a>c:

    print("A is the largest number")

elif b>a and b>c:

    print("B is the largest number")

else:
    print("C is the largest number")
"""
#Enter the choice program
"""
a = float(input("Enter the value for a"))
b = float(input("Enter the value for b"))

x = float(input("Enter the choice is 1,2,3,4:"))

if x==1:
    print("Addition:",a+b)
elif x==2:
    print("Subtraction:",a-b)
elif x==3:
    print("Division",a*b)
elif x==4:
    print("Multiplication:",a*b)
"""

# Looping

# do while loop
"""
i = 10

while i>=1:
    print(i)
    i-=1
"""
# all even numbers while loop
"""
i = 1

while i<=10:
    if i % 2==0:
        print(i)
    i += 1
"""
# Table of number
"""
num = int(input("Enter the number"))
i = 1
while i<=10:
    print(num*i)
    i+=1
"""
#program to find factorial of number

"""
f = 1
num = int(input("Enter the number"))
i = 1
while i<=num:
    f = f*i
    i+=1
print("factorial=",f)

"""
# sum of the number
"""
s = 0
i = 1
num = int(input("Enter the number"))

while i<=num:
    s = s+i
    print("Sum",s)
    i+=1
"""
"""
#For Loop

for i in range(1,100):
    if i%2==0:
        print(i)
"""

#program to print 1 to 6 in for loop

"""for i in range(1,6):
    print(i)
"""
"""
# program to print even numbers to 2 to 10

for i in range(2,11,2):
    print(i)
"""
"""
num = int(input("Enter the number"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
"""

# for loop sum of the num 1 to n
"""
n = int(input("Enter the number"))

s = 0

for i in range(1,n+1):
    s+=1
    print("Sum=",s)
"""
# Nested for loop
# program to print right angle triangle:
"""
rows = 5
for i in range(1,rows+1):
    for j in range(i):
        print('*', end ="")
    print()
"""
# program to print number right angle triangle:

rows = 5
for i in range(1,rows+1):
    for j in range(i):
        print(j+1, end = "")
    print()















