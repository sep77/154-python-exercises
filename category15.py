# 129- write a program that takes two numbers from the user as an interval and displays
# all the prime numbers in that interval.

lower_num = int(input("Enter the lower num:"))
upper_num = int(input("Enter the upper num:"))

if lower_num < upper_num:
    print(f"The prime numbers between{lower_num} & {upper_num} are:")
    for num in range(lower_num, upper_num+1):
        if num > 1:
            for i in range(2, num):
                if (num % i == 0):
                    break
            else:
                print(num)

elif lower_num == upper_num:
    print("Numbers can not be equal.")

else:
    print("First num can not be greater.")


# 130- write a program that takes a number from the user and returns the factorial.

number = int(input("Number:"))
if number < 0:
    print("can not be negative")
elif number == 0:
    print("factorial of zero is 1")
else:
    factorial = 1
    for i in range(1, number+1):
        factorial *= i

    print(f"Factorial of {number} is {factorial}")


# 131- write a program that takes a number from the user and displays the
# multiplication table or sequence for that number starting at 1
# and ending at 10 .

number = int(input("num:"))

for x in range(1, 11):
    print(f"{number} x {x} = {number * x}")


# 132- write a program that takes the number of terms in the fibonacci sequence
# from the user and displays the sequence.

x1, x2 = 0, 1
count = 0

term = int(input("enter term:"))

if term <= 0:
    print("please enter a positive integer.")

elif term == 1:
    print("the fibonacci of 1 is:")
    print(x1)

else:
    print("the fibonacci sequence is:")

    while count < term:
        print(x1)

        nth = x1 + x2

        x1 = x2
        x2 = nth
        count += 1


# 133- display a number in an armstrong number.

# for example : 153 = 1*1*1 + 5*5*5 + 3*3*3
# 9743 = 9*9*9*9 + 7*7*7*7 + 4*4*4*4 + 3*3*3*3

number = int(input("number::"))
# * len integer tahvil mide ama voroodi byad string bshe.
order = len(str(number))
temp_value = number
sum = 0

while temp_value > 0:
    digit = temp_value % 10
    sum += digit ** order

    temp_value //= 10

if sum == number:
    print("an armstrong number")
else:
    print("not an armstrong number")


# 134- sum of all natural numbers up to that number.

number = int(input("natural of:"))

if number < 0:
    print("wrong")

else:
    sum = 0
    while number > 0:
        sum += number
        number -= 1


# 135- write a program that inputs a number and displays the successive powers of 2 up to that number.

numbers = int(input("number:"))

result = list(map(lambda x: 2 ** x, range(numbers)))
print(result)
