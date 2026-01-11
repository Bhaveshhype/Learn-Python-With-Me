i=0
for i in range(1,100):
    print(i)


i =0
for i in range(1,100):
    if i % 2 == 0:
        print("the number is even",i)

x=0
for x in range (10):
    print("Hello World")
    x=x+1
    print(x)

x=0
for x in range (0,9):
    print("Natural Number")
    x=x+1
    print(x)

i=0
for i in range(0,10):
    i=i+1
    print(i)

sum = 0
for i in range(1,101):
    sum += i
print(sum)

i=0
for i in range (125):
    print(i)
    if i % 3 and i % 7:
        print("the number is divisible by 3 and 7")
    elif i % 3 :
        print("the number is divisible by 3")
    elif i % 7 :
        print("the number is divisible by 7")
    else:
        print("the number is not divisible by 3 and 7")

for i in range(1,11):
    print("5 X", i ,"=",i*5)

import math
i=0
for i in range(1,11):
    print(i,":- Square root is",math.sqrt(i))



sum of even numbers
sum=0
for i in range(2,21,2):
    sum += i
print(sum)

# from math import factorial
import math
import factorial
n=5
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
    print(factorial)

n=10
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
    print(factorial)

fibonacci series: 0+1=1, 1+1=2, 2+1=3, 3+2=5,5+3=8, 8+5=13

num1,num2=0,1
print("fibonacci series:")
for i in range(10):
    print(num1,end=" ")
    result = num1+num2
    num1=num2
    num2=result
# ***********************888
n = int(input("Enter a number: "))
rev=" "
for char in reversed(str(n)):
    rev = rev + char
if reversed(str(n)) == str(n):
    print("Yes, the number is reverse "+rev)
else:
    print("No, the number is not reverse "+rev)
# ************************************************************************8
palindrome number***********************889
n= int(input("Enter a number: "))
original =n
rev=0
digit=len(str(n))

for i in range(digit):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if rev==original:
    print('no is palindrome')
else:
    print('no is palindrome')

# ********************************************
Armstrong numbers
153= 1**3+5**3+3**3 = 153
n=int(input("Enter a number: "))
sum=0
for digit in str(n):
    sum +=int(digit)**3
if sum==n:
    print("armstrong number is ",n)
else:
    print("not armstrong number")

perfect number
n= int(input("Enter a number: "))
sum = 0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print(n,"number is perfect")
else:
    print(n,"number is not perfect")

Star Patterns
for i in range(1,5):
    print("*"*i)

for i in range(4,0,-1):
    print("*"*i)

for i in range(1,5):
    for j in range (1,i+1):    #pattterns
        print(j,end=" ")
    print()

rows = 4
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2*i - 1))
# ********************************************************************
rows = [5, 4, 3, 2, 1]
num=1
for count in rows:
    print(str(num)*count)
    num=num+1
or

rows=5
b=0
for i in range(rows,0,-1):
    b=b+1
    for j in range(1, i+1):
        print(b,end=" ")
    print()
# *************************************************************************

rows = [5, 5, 5, 5, 5]
num = 1
for count in rows:
    num *= count
    print(num)

# **********************************************8
rows = [5, 5, 5, 5, 5]
num = 1
for count in rows:
    print(str(num)*count)
    num+=1

# ********************************************************************************
WHILE LOOP ******
i=1
while i<=5:
    print(i)
    i=i+1

Even Number
num=2
while num<100:
    print(num)
    num=num+2

num=1
while num<100:
    print(num)
    num=num+2

i=1
total=0
while i<=5:
    total=total+i
    i=i+1
print("sum:-",total)
# *********************************************fibonaci series
num = int(input("Enter a number: "))
Factorial =1
i=1
while i <= num:
    Factorial = Factorial * i
    i = i + 1
print(num,"=" ,Factorial)


number = int(input("Enter a number: "))
A=0
B=1
counter=0
while counter < number:
    print(A, end=" ")
    C =A + B
    A = B
    B = C
    counter = counter + 1

