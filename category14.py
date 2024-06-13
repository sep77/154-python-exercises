import random
import cmath
# 119- write a program that takes two numbers from the user, adds them together
# and show the result.
"""
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

result = num1 + num2
print(f"the result is: {result}")
"""

# 120- write a program that takes a number from the user, calculates and displays
# the square root of that number.
"""
x = int(input("Enter Number:"))

result = round(x ** 0.5, 2)  #********** ta 2 ragham ashar minevise
print(f"the square root is: {result}")

"""

# 121- calculate the area of the triangle with Heron's formula.
"""
side1 = int(input("side1:"))
side2 = int(input("side2:"))
side3 = int(input("side3:"))

semi_perimeter = (side1 + side2 + side3) / 2
triangle_area = (semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) *
(semi_perimeter - side3)) ** 0.5

print(f"the area of triangle is {triangle_area}")
"""

# 122- write a program that takes user inputs for three constants of a quadratic equasion
# solves the equasion and displays the solutions.

# import math
# import cmath  ---> agar javab moadele adad sahih nmishe in ro bzn
"""
a = int(input("a:"))

if a <= 0:
    print("a can not be zero or less.")

else:
    b = int(input("b:"))
    c = int(input("c:"))

discriminant = (b ** 2) - (4 * a * c)

solution1 = (-b - cmath.sqrt(discriminant)) / (2*a)
solution2 = (-b + cmath.sqrt(discriminant)) / (2*a)

print(f"The solutions are {solution1} & {solution2}")
"""


# 123- write a program that takes two numbers from the user, stores them inside variables and then
# swaps the variables values in two ways:

# (1) by using a temporary value
# (2) by not using a temporary value

# at the end, display the results to the user.
"""
x = input("Enter Anything :")
y = input("Enter Anything:")

print(f"Before swapping, first anything is '{x}' & second anything is '{y}'")


# Approach 1
temp = x
x = y
y = temp

print(f"After swapping first anything is '{x}' & second anything is '{y}'")

# Approach 2

x,y = y,x
"""


# 124- write a program that generates random numbers between 1 and 100 .
# import random
print(f"random numbers between 1 and 100 :", random.randint(1, 100))


# 125- write a program that takes an input from the user as a number and displays
# to the whether the input number is a positive number or not.

# solve in two ways :
# (1) using if ... elif ... else statement
# (2) using nested conditionals


"""
# Approach1
a = int(input("Enter a number:"))

if (a > 0):
    print("You have entered a positive number.")

elif a == 0:
    print("You have entered zero number.")

else:
    print("You have entered a negative number.")


# Approach2
if a >= 0:
    if a > 0:
        print("positive")
    else:
        print("zero")
else:
    print("negative")
"""

# more advanced way


def input_number():
    a = int(input("Enter a number:"))

    if (a > 0):
        print("You have entered a positive number.")

    elif a == 0:
        print("You have entered zero number.")

    else:
        print("You have entered a negative number.")


try:
    input_number()
# ** momkene chizi gheyr az adad vared she va in except hame chiz ro shamel mishe.
except:
    print("please enter a valid number")


# 126- write a program that takes a year as an input and displays to the user
# if the year represents a leap year or not.

# **** leap year har 4 sal yekbar hast va sali ke century year hast
# **** ham baz har 4 dor yekbar hast.
"""
year = int(input("Enter year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year ")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")

"""


# 127- write a program that takes three different numbers and displays the largest.
"""
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))

if (num1 > num2) and (num1 > num3):
    num_largest = num1

elif (num2 > num1) and (num2 > num3):
    num_largest = num2

else:
    num_largest = num3

if num1 == num2 == num3:
    print("enter different numbers.")

else:
    print("The largest number is :", num_largest)
"""

# 128- prime number
number = int(input("Enter number:"))

if number > 1:
    for x in range(2, number):
        if (number % x == 0):
            print(number, "is not a prime number.")
            print(x, "times", round(number/x), "is", number)
            break
    else:
        print(number, "is a prime number.")


else:
    print("not a prime number.")
