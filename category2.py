# 16- Accept two numbers from the user and calculate their multiplication.
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))

result = num1 * num2
print(result)


# 17- display "my name is jane" as "my**name**is**jane" using output formatting of the print() function".

print("my", "name", "is", "jane", sep="**")


# 18- Display float number with 2 decimal places using print().

print("%.2f" % 45.34789)


# 19- Accept a list of numbers and the size of the list as an input from the user.


float_nums = []

list_nums = int(input("plese enter the list size:"))

for i in range(0, list_nums):

    print("the number at location", i, ":")

    item = float(input())
    float_nums.append(item)

print("The user list is:", float_nums)
