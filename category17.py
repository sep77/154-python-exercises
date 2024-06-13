# 143- write a program that displays a calendar for a specified year
# and month entered by the user.

# import calendar
import calendar
year = int(input(" year:"))
month = int(input("month:"))

print(calendar.month(year, month))


# 144- write a program that takes the number of terms to be displayed in the fibonacci sequence
# from the user and returns the modified sequence using recursion.

def fibo(n):
    if n <= 1:
        return n
    else:
        result = fibo(n-1) + fibo(n-2)
        return result


terms = int(input("please Enter terms:"))

if terms <= 0:
    print("please enter a positive number")
else:
    print("the fibonacci sequence is:")

    for x in range(terms):
        print(fibo(x))


# 145- Displays the sum of all natural numbers up to that number using recursion.

def recur_nat(n):
    if n <= 1:
        return n
    else:
        return n + recur_nat(n-1)


number = int(input("Enter number:"))

if number <= 0:
    print("please enter a positive integer")
else:
    print("The sum is", recur_nat(number))


# 146- Finding the factorial of a number using recursion.
number = int(input("Enter number for factorial:"))


def recur_fact(n):
    if n == 1:
        return n
    else:
        return n * recur_fact(n-1)


if number < 0:
    print("Enter positive")

elif number == 0:
    print("The factorial of zero is 1")

else:
    print("The factorial of", number, "is", recur_fact(number))


# 147- write a program that transposes a matrix in two different ways.
# 1. nested loop
# 2. using nested list comprehension

# 3x2 matrix
x = [[1, 7],
     [4, 5],
     [7, 8]]

# Approach 1 --> using nested loops
result = [[0, 0, 0],
          [0, 0, 0]]

for row in range(len(x)):
    for col in range(len(x[0])):
        result[col][row] = x[row][col]

for data in result:
    print(data)

# Approach 2 --> nested list comprehension
result = [[x[col][row]
           for col in range(len(x))] for row in range(len(x[0]))]


# 148- write a program that adds two matrices in two different ways.
# 1. Nested loop
# 2. nested list comprehension

# 3x3 matrix
x = [[1, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[1, 9, 1],
     [6, 7, 3],
     [4, 5, 9]]


# Approach1
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(len(x)):
    for col in range(len(x[0])):
        result[row][col] = x[row][col] + y[row][col]


# Approach2
result = [[x[row][col] + y[row][col]
           for col in range(len(x[0]))] for row in range(len(x))]
print(result)


# 149- write a program that multiplies two matrices in two different ways.
# 1. Nested loop
# 2. nested list comprehension

x = [[1, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[1, 6, 9, 3],
     [2, 5, 4, 8],
     [3, 5, 2, 1]]

# Approach1

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# iteratin through rows of x
for i in range(len(x)):
    # iterating through col of y
    for j in range(len(y[0])):
        # iterating through rows of y
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]
print(result)
