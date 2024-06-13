# 20- print the first 10 natural numbers using while loop.

num = 0

while num <= 10:
    print(num)
    num += 1

print("\t")
# 21- print the following pattern

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""

last_num = 6

for row in range(1, last_num):

    for column in range(1, row + 1):

        print(column, end=" ")

    print(" ")


# 22- Accept number from user and calculate the sum of all numbers from 1 to a given number.
"""
given_number = int(input("enter number:"))

sum_number=0
for num in range(1,given_number + 1, 1):

    sum_number += num

print(sum_number)

"""

# 23- print the multiplication table for a number.

num = 5

for i in range(1, 11, 1):
    product = i * num
    print(product)

# 24- Iterate the list below, and display numbers divisible by 5, and stop the iteration
# when hitting a number of greater than 100 in the list.

List = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for item in List:
    if (item > 100):
        break

    if (item % 5 == 0):
        print(item)


# 25- count the total number of digits in a number.

count = 0
number = 6578235
while number != 0:
    number = number // 10
    count += 1

print("the total digits:", count)


# 26- print the following pattern using for loop.

"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1 
1
"""
for row in range(6, 0, -1):
    for column in range(row - 1, 0, -1):
        print(column, end=" ")

    print("")


# 27- reverse the following list using for loop.

List = [10, 20, 30, 40, 50]

for i in range(len(List) - 1, -1, -1):
    print(List[i])


# 28- Display numbers from -10 to -1 using for loop.

for num in range(-10, 0, 1):
    print(num)


# 29- Display a message "Done" after successful execution of a for loop.
for i in range(5):
    print(i)

else:
    print("Done!!!!")


# 30- write a program to display all prime numbers within a range.
start = 25
stop = 50

print(f"Prime Numbers Between {start} and {stop} are:")

for num in range(start, stop + 1):
    for i in range(2, num):
        if (num % i == 0):
            break
    else:
        print(num)

# 31- use a loop to display elements from the given list that are present at odd index positions.
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in my_list[1::2]:
    print(i, end=" ")


# 32- Display the cube of the number up to a given integer.

input_num = 6

for i in range(1, input_num + 1):
    print(f"the number is {i} and the cube is : {i*i*i}")


# 33- print the following pattern.

"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
for row in range(1, 6):
    for column in range(1, row + 1):
        print("*", end=" ")
    print("\r")

for row in range(5, 0, -1):
    for column in range(0, row - 1):
        print("*", end=" ")

    print("\r")
