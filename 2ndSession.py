# percentage over the marks
M1 = float(input("Enter first number: "))
M2 = float(input("Enter second number: "))
M3 = float(input("Enter third number: "))
M4 = float(input("Enter fourth number: "))
M5 = float(input("Enter fifth number: "))
total = M1 + M2 + M3 + M4 + M5
print(total)
Percent = (total/500)*100
print(Percent)

# area of rectangle
Length = float(input("Enter the length of rectangle: "))
Breadth = float(input("Enter the breadth of rectangle: "))
Area = (Length*Breadth)
print(Area)

# Area of Circle
Pie = 3.14
Radius = int(input("Enter the radius : "))
R = Radius*Radius
Area = Pie * R
print(Area)

principle = float(input("Enter the principle: "))
Rate = float(input("Enter the rate: "))
time = float(input("Enter the time: "))
SI = principle*Rate*time/100
print(SI)

# Conditionals

A = int(input("Whats A"))
B = int(input("Whats B"))
if A > B:
    print("A is greater than B")
else:
    print("B is greater than A")
if A < B:
    print("A is less than B")
else:
    print("B is less than A")

A = int(input("Enter A: "))
B = int(input("Enter B: "))
if A % 2 == 0:
    print("Even")
else:
    print("Odd")
if B % 311 == 0:
    print("Odd")
else:
    print("Even")

marks = int(input("Enter marks: "))
if marks > 90:
    print("passed with A+")
elif marks >= 80:
    print("passed with B")
elif marks >= 70:
    print("passed with C")
else:
    print("Failed")

age = int(input("Enter your age: "))
has_ID = True
if age >=18:
    if has_ID:
        print("Entry Allowed")
    elif age < 18:
        print("ID Required")
    else:
        print("Entry Not Allowed")

