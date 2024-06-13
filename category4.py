# 34- create a function that can accept two arguments name and age and print their value.

def demo(name, age):
    print(name, age)


demo("Ben", 25)

# 35- write a function such that it accepts a variable length of argument and print all
# arguments value.


def func(*arg):
    for i in arg:
        print(i)


func(10, 20, 0)

# 36- write a function calculation such that it can accept two variables and calculate the addition
# and subtraction of them and also it must return both addition and subtraction
# in a single return call.


def calculation(a, b):
    return a+b, a-b


print(calculation(40, 10))


# 37- create a function show Employee() such that it should accept employee name, and its salary
# and display both. if the salary is missing in the function call assign default value 9000
# for salary by default.

def show_employee(name, salary=9000):
    print(f"{name} has a salary of {salary}")


show_employee("john", 12000)

# 38-
"""
create an inner function to calculate the addition in the following way:
create an outer function that will accept two parameters , a and b
create an inner function inside the outer function that will calculate the addition of a and b
At last, the outer function will add 5 into addition and return it.
"""


def outer_function(a, b):

    def inner_function(a, b):
        return a + b

    add = inner_function(a, b)

    return add + 5


result = outer_function(5, 10)
print(result)

# 39- write a recursive function to calculate the sum of numbers from 0 to 10.


def calculate_sum(num):
    if num:
        return num + calculate_sum(num - 1)

    else:
        return 0


print(calculate_sum(100))


# 40- Assign a different name to a function and call it with the new name.

def display_student(name, age):
    print(name, age)


show_student = display_student

show_student("emma", 24)


# 41- Generate a python list of all the even numbers between 4 and 30.
print(list(range(4, 30, 2)))
