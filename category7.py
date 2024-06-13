# 59- concatenate two lists index-wise.
List1 = ["M", "na", "i", "ke"]
List2 = ["y", "me", "s", "lly"]

list3 = [i+j for i, j in zip(List1, List2)]
print(list3)

# 60- Given a python list of numbers, turn every item of a list into its square.

List = [1, 2, 3, 4, 5, 6, 7]

List = [x * x for x in List]

print(List)


# 61- concatenate two lists in the following order.
list1 = ["hello", "hi"]
list2 = ["dear", "sir"]

["hello dear", "hello sir", "hi dear", "hi sir"]

result = [x + y for x in list1 for y in list2]
print(result)

# 62- Given the below two lists, Iterate both lists simultaneously such that
# list1 should display item in original order and list2 in reverse order.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

print("\n")

# 63- Add item 7000 after 6000 in the following list.

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)

print("\n")

# 64- Given a nested list extend it by adding the sub list ["h","i","j"] in such a way that
# it will look like the following list.

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)


# 65- find value 20 in the list, and if it is present replace it with 200.
# only update the first occurence of a value.

List = [5, 10, 15, 20, 25, 50, 20]

index = List.index(20)
List[index] = 200

print(List)


# 66- Remove all occurence of 20 from the list.
List = [5, 20, 15, 20, 25, 50, 20]


def remove_value(List, val):
    return [value for value in List if value != val]


result_list = remove_value(List, 20)
print(result_list)
