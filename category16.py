# 136- write a program that takes a divisor, a dividend lower limit and a dividend upper limit from the
# user and returns the numbers divisible by the divisor in the dividend range.

import itertools
import random
dividend_lower_limit = int(input("Enter lower limit:"))
dividend_upper_limit = int(input("Enter upper limit:"))
divisor = int(input("Enter Divisor:"))

if dividend_lower_limit > dividend_upper_limit:

    print("Dividend lower limit can not be bigger than upper limit.")

elif dividend_lower_limit == dividend_upper_limit:
    print("please Enter different numbers.")

elif dividend_upper_limit < divisor:
    print("Dividend upper limit can not be smaller than divisor.")

elif divisor <= 0:
    print("divisor can not be zero or negative.")

else:
    number_range = [x for x in range(
        dividend_lower_limit, dividend_upper_limit+1)]

    result = list(filter(lambda y: (y % divisor == 0), number_range))
    print(f"Numbers Divisible by {divisor} are:")

    for z in result:
        print(z)


# 137- write a program that takes a character from the user and returns the ASCII value of it.
character = input("Enter a character:")
ascii_value = ord(character)
print(f"ASCII value of {character} is {ascii_value}")


# 138- write a program that takes two numbers and returns the highest common factor (H.C.F)
# OR greatest common divisor (G.C.D) of the numbers.
# it is the largest positive integer that  perfectly divides the two given numbers, the HCF of 12 and 14 is 2.
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))

if number1 <= 0 or number2 <= 0:
    print("Entered Numbers can not be zero or less.")

else:
    def calculate_HCF(number1, number2):
        if number1 > number2:
            smallest = number2
        else:
            smallest = number1
        for x in range(1, smallest + 1):
            if (number1 % x == 0) and (number2 % x == 0):
                HCF = x
        return HCF
    print("The HCF is :", calculate_HCF(number1, number2))


# 139- write a program that takes two numbers and returns the Least common Multiple (L.C.M).
# It is the smallest positive integer that is perfectly divisible by the two given numbers,
# For example, the LCM of 12 and 14 is 84.
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))

if number1 <= 0 or number2 <= 0:
    print("Entered Numbers can not be zero or less.")

else:
    def calculate_LCM(number1, number2):
        if number1 > number2:
            greater = number1
        else:
            greater = number2
        while greater:
            if (greater % number1 == 0) and (greater % number2 == 0):

                LCM = greater
                break
            greater += 1
        return LCM

    print("The LCM is:", calculate_LCM(number1, number2))


# 140- Return the factor of a number.
number = int(input("Enter numb:"))
if number <= 0:
    print("please enter a positive integer.")

else:
    def factor(num):
        print(f"the factors of {num} are:")
        for x in range(1, num+1):
            if (num % x == 0):
                print(x)
    factor(number)


# 141- Takes from user an arithmetic operation, then returns the result based on two numbers.

def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


print("please select an operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

number_input = int(input("Please Enter Your Choice (1/2/3/4):"))

while True:
    if number_input in (1, 2, 3, 4):

        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))

        if number_input == 1:
            print(f"{num1} + {num2} = {addition(num1,num2)}")
        elif number_input == 2:
            print(f"{num1} - {num2} = {subtraction(num1,num2)}")
        elif number_input == 3:
            print(f"{num1} x {num2} = {multiplication(num1,num2)}")
        elif number_input == 4:
            if num2 == 0:
                print("Can not divide by zero.")
            else:
                print(f"{num1} / {num2} = {round(division(num1,num2),2)}")
        break
    else:
        print("Invalid operation")


# 142- write a program that creates a deck of cards shuffles it each time the program is run.

# import random
# import itertools

deck = list(itertools.product(range(1, 14), [
            "Heart", "Spade", "Diamond", "Club"]))

random.shuffle(deck)

for card in range(4):

    print(deck[card][0], "of", deck[card][1])

    # print(deck[card]) --> fght haminm mishe balayo namayeshesh behtre.
