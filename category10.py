# 88- Reverse the following tuple.
tuple = (10, 20, 30, 40, 50)

tuple = tuple[::-1]
print(tuple)


# 89- Access value 20 from the following tuple.

tuple = ("orange", [10, 20, 30], (5, 15, 25))

print(tuple[1][1])


# 90- create a tuple with a single item 50.

tuple = (50,)
print(tuple)


# 91- unpack the following tuple into 4 variables.
tuple = (10, 20, 30, 40)

a, b, c, d = tuple
print(a)
print(b)
print(c)
print(d)

# 92- swap the following two tuples.
tuple_one = (11, 22)
tuple_two = (99, 88)

tuple_one, tuple_two = tuple_two, tuple_one

print(tuple_one)
print(tuple_two)


# 93- copy elements 44 and 55 from the following tuple into a new tuple.
tuple = (11, 22, 33, 44, 55, 66)

tuple_two = tuple[3:-1]  # az 3 ta -1 ke khod -1 ke 66 hast hesab nmishe.
print(tuple_two)


# 94- change the value of the first item of a list to 222.
tuple = (11, [22, 33], 44, 55)

tuple[1][0] = 222
print(tuple)


# 95- count the number of occurences of item 50 from a tuple.
tuple = (50, 10, 60, 70, 50)

print(tuple.count(50))
