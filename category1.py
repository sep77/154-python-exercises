# 1- print the result of the multiplication of two sets of integers if it is less than 1000.
# If the result is greater than 1000, print their sum.

num1 = 25
num2 = 26

num1 = 35
num2 = 36


def multi_or_sum(num1, num2):
    product = num1 * num2

    if product <= 1000:
        return product

    else:
        return num1+num2


result = multi_or_sum(25, 26)
print(result)
result1 = multi_or_sum(35, 36)
print(result1)

# 2- Iterate from the start number to the end number of the first 10 numbers
# and in each Iteration print the sum of the current number with the previous number.


def sum_num(num):
    previous_num = 0

    for number in range(num):
        sum = previous_num + number

        print("current_num:", number, "previous_num:", previous_num, "sum:", sum)
        previous_num = number


sum_num(10)

# 3- In a string, display the characters at the even indices.


def even_indices(str):

    for char in range(0, len(str), 2):

        print("Index[", char, "]", str[char])


string = "learning"
even_indices(string)

# 4- Given a string and an integer number n , remove characters from a string starting
# from zero up to n , and return a new string.


def remove_chars(str, num):

    return str[num:]


print(remove_chars("learning", 4))


# 5- Given a list of numbers, return True if first and last number of a list is the same

list1 = [10, 20, 30, 40, 10]
list2 = [10, 20, 30, 40, 50]


def first_last_same(list):
    print("Given List:", list)

    first_el = [0]
    last_el = [-1]

    if first_el == last_el:
        return True
    else:
        return False


test_list = [10, 20, 30, 40, 10]

print("result:", first_last_same(test_list))


# 6- Given a list of numbers, Iterate it and print only those numbers which are divisible by 5.
List = [10, 20, 33, 46, 55, 77, 105, 204, 335]


def divisible_by_5(num_list):
    print("Given list:", num_list)

    for num in num_list:
        if (num % 5 == 0):
            print("Divisible by 5 :", num)


divisible_by_5(List)

# 7- Return the count of how many times the sub_string "katie" appears in the given string.
str = "katie is good developer. katie is a writer."

print(str.count("katie"))

# 8- print the following pattern

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

for num in range(6):
    for i in range(num):
        print(num, end=" ")

    print("\n")

# 9- Reverse a given number and return True if it is the same as the original number.
num1 = 323
num2 = 625


def reverse_number(number):
    original_num = number
    reverse_num = 0

    while (number > 0):
        remainder = number % 10

        reverse_num = reverse_num * 10 + remainder
        number = number // 10

    if original_num == reverse_num:
        return True
    else:
        return False


print("original is the same as the Reversed:", reverse_number(626))

print("\n")
# 10- Given two lists of numbers, create a new list such that the new list should contain
# only odd numbers from the first list and even numbers from the second list.

list_1 = [10, 20, 23, 11, 17, 44, 55]
list_2 = [13, 43, 24, 36, 12, 33, 66]


def merge_list(list_one, list_two):
    list_three = []

    for num in list_one:
        if (num % 2 != 0):
            list_three.append(num)

    for num in list_two:
        if (num % 2 == 0):
            list_three.append(num)

    return list_three


print("merged list is:", merge_list(list_1, list_2))

print("\n")
# 11- write a code to extract each digit from an integer in the reverse order.
integer = 33154689

print("given number:", integer)

while integer > 0:
    digit = integer % 10

    integer = integer // 10
    print(digit)


# 12- calculate tax income for the given income by following to the below rules.
"""
taxable income      rate (in %)
first 10000         0
next 10000          10
the remaining       20
"""
income = 45000
tax_payable = 0

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    tax_payable = (income - 10000) * 10 / 100

else:
    tax_payable = 0
    tax_payable = (10000) * 10 / 100

    tax_payable += (income - 20000) * 20 / 100

print("total payable tax amount is:", tax_payable)


# 13- print multiplication table from 1 to 10 .

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\t\t")

# 14- print downward half-pyramid pattern with star (asterisk).

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end="")
    print("")


# 15- write a function called exponent(base , exp) that returns an int value of base raises
# to the power of exp.

def base_power(base, power):
    num = power
    result = 1

    while num > 0:
        result = result * base
        num = num - 1

    print(base, "to the power of ", power, "is", result)


base_power(4, 5)
