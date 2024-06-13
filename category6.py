# 51- Given two lists create a third list by picking odd-index elements from the first list
# and even-index elements from the second.

list_one = [3, 6, 9, 12, 15, 18, 21]
list_two = [4, 8, 12, 16, 20, 24, 28]

list_three = list()

odd_elements = list_one[1::2]
even_elements = list_two[0::2]

list_three.extend(odd_elements)
list_three.extend(even_elements)

print(list_three)

print("\t")

# 52- Given a list, remove the element at index 4, and add it to the 2nd position and at
# the end of the list.

List = [34, 56, 23, 11, 89, 78, 345]

target_element = List.pop(4)
print(target_element)

List.insert(2, target_element)
print(List)

List.append(target_element)  # be akhar ham ezafe mikone.
print(List)


# 53- Iterate a given list and count the occurence of each element and create a dictionary
# to show the count of each element.

sample_list = [2, 9, 23, 9, 46, 78, 9, 46, 46]

element_count = dict()

for item in sample_list:
    if item in element_count:

        element_count[item] += 1

    else:
        element_count[item] = 1

print(element_count)


# 54- Given a two lists of equal size create a python set such that it shows the elements
# from both lists in the pair.

List_one = [2, 3, 4, 5, 6, 7, 8]
List_two = [4, 9, 16, 25, 36, 49, 64]

result = zip(List_one, List_two)

result_set = set(result)
print(result_set)

print("\n")
# 55- Given the following two sets find the intersection and remove those elements
# from the first set.

set1 = {65, 42, 78, 83, 23, 57, 29}

set2 = {67, 73, 43, 48, 83, 57, 29}

intersection = set1.intersection(set2)
print(intersection)

for item in intersection:
    set1.remove(item)

print(set1)

print("\n")
# 56- Given two sets, check if one set is a subset or superset of another set. if the subset
# is found delete all elements from that set.

firstset = {27, 43, 34}
secondset = {34, 93, 22, 27, 43, 53, 48}

print("first set is the subset of the second set:", firstset.issubset(secondset))
print("second set is the subset of the first set:", secondset.issubset(firstset))

print("first set is the super set of the second set:",
      firstset.issuperset(secondset))
print("second set is the superset of the first set:",
      secondset.issuperset(firstset))

if firstset.issubset(secondset):
    firstset.clear()

if secondset.issubset(firstset):
    secondset.clear()

print(firstset)
print(secondset)

print("\n")
# 57- Iterate a given list and check if a given element already exists in a dictionary
# as a key's value if not delete it from the list.

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

rollNumber[:] = [item for item in rollNumber if item in sampleDict.values()]

print(rollNumber)

print("\n")
# 57- Given a dictionary get all values from the dictionary and add them to a list
# but don't add duplicates.

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44,
         'may': 52, 'june': 53, 'july': 54, 'Aug': 44, 'sept': 54}

speed_list = list()

for item in speed.values():
    if item not in speed_list:
        speed_list.append(item)

print(speed_list)


# 58- Remove duplicates from a list and create a tuple and find the minimum and max number.

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

List = list(set(speed_list))  # sets are unique elements.

tuple = tuple(List)

print("min:", min(tuple))
print("max:", max(tuple))
