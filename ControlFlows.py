Marks = int(input("Enter the Marks"))
if Marks>=90:
    print("The Grade is A+")
elif Marks>80:
    print("the Grade is A ")
elif Marks>70:
    print("the Grade is B ")
elif Marks>60:
    print("the Grade is C ")
else:
    print("the Student is Failed in Exam ")

# Entry Eligibility:
Age = int(input("Enter the Age"))
if Age>18:
    print("Entry Allowed")
elif Age==18:
    print("ID Require")
else:
    print("Entry Not Allowed")

show, whether the integer is positive or negative
integer = int(input("Enter a number: "))
if integer<0:
    print("The integer negative.")
else:
    print("The integer positive.")

Numbr = int(input("Enter a number: "))
if Numbr % 2 == 0:
    print(Numbr, "is even")
else:
    print(Numbr, "is odd")

Multiple: ***
number = int(input("Enter a number: "))
if number % 5 == 0:
    print(number, "is a multiple of 5")
else:
    print(number, "is not a multiple of 5")

# *******************************************************************

S1 = int(input("Enter the mark in 1st Subject"))
S2 = int(input("Enter the mark in 2nd Subject"))
S3 = int(input("Enter the mark in 3rd Subject"))
S4 = int(input("Enter the mark in 4th Subject"))
S5 = int(input("Enter the mark in 5th Subject"))
total = S1 + S2 + S3 + S4 + S5
print(total)

percentage = (total/500)*100
print(percentage)

if percentage>=90:
    print("You are  O+")
elif percentage>=80:
    print("You are A+")
elif percentage>=70:
    print("You are B+")
else:
    print("You are C")

# Monthwise-regression

M = int(input("Enter the number of month: "))
if M == 1:
    print("The month is January")
elif M == 2:
    print("The month is February")
elif M == 3:
    print("The month is March")
elif M == 4:
    print("The month is April")
elif M == 5:
    print("The month is May")
elif M == 6:
    print("The month is June")
elif M == 7:
    print("The month is july")
elif M == 8:
    print("The month is August")
elif M == 9:
    print("The month is September")
elif M == 10:
    print("The month is October")
elif M == 11:
    print("The month is November")
elif M == 12:
    print("The month is December")
else:
    print(" no matched found")

# balance ==10, input as amount, it should be less thn 0, amount is greater than balanced== insufficient balance,
# amount is % 100!= 0 the amount must be in multiple of 100, otherwise withdrwal successful

Balance = 10000
Amount = int(input("Enter Amount Amount: "))
if Amount > Balance:
    print("Aukaat mai Rehle Mittar!!!!!")
elif Amount %100 != 0:
    print("The Amount Must Be Multiple of 100")
else:
    print("Withdraw is Successful")

Check Given alphabet is vowel or consonent
ch= input("Enter the Character : ")
if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonent" )

largest of 3 numbers
Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
Num3 = int(input("Enter the third number: "))
if Num1 > Num2 and Num1 > Num3:
    print("larger Number is",Num1)
elif Num2 > Num3 and Num2 > Num1:
    print("Larger Number is",Num2)
else:
    print("larger Number is",Num3)

# prime number
Num1 = int(input("Enter the first number: "))
if Num1 % 1 == Num1 and Num1>0:
    print(Num1,"Number is Prime")
else:
    print(Num1,"Number is Negative")

# create the program for number that is divisible by 3 & 7 #
num1 = int(input("Enter the first number: "))
if num1 % 3 == 0 and num1 % 7 == 0:
    print("The number is divisible by 3 and 7")
elif num1 % 3 == 0:
    print("The number is only divisible by 3")
elif num1 % 7 == 0:
    print("The number is only divisible by 7")
else:
    print("The number is not divisible by 3 And 7")
# 
Amount = float(input("Enter the Amount: "))
if Amount>5000:
    discount = Amount*0.20
    print("The Total Amount is:",Amount-discount)
elif Amount>3000:
    discount = Amount*0.15
    print("The Total Amount is:",Amount-discount)
elif Amount>1000:
    discount = Amount*0.10
    print("The Total Amount is:",Amount-discount)
else:
    print("The total Amount is:",Amount)

# Gross Salary
# DA = 10%, TA = 12%, HRA = 15%
# (Dearness Allowance, Travelling Allowance,House Rent Allowance)
basic = float(input("Enter basic salary: "))
da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic
total_salary = basic + da + ta + hra
print("Total Salary =", total_salary)
