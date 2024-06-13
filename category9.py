# 79- Add a list of elements to a given set.

sample_set = {"yelloe", "orange", "black"}
sample_list = ["blue", "green", "red"]


sample_set.update(sample_list)
print(sample_set)


# 80- Return a new set of identical items from given two sets.

set_one = {10, 20, 30, 40, 50}
set_two = {30, 40, 50, 60, 70}

print(set_one.intersection(set_two))


# 81- Return a new set with all items from both sets by removing duplicates.

set_one = {10, 20, 30, 40, 50}
set_two = {30, 40, 50, 60, 70}

set_three = set_one.union(set_two)
print(set_three)


# 82- Given two sets, update the first set with items that exist only in the first set
# and not in the second set.

set_one = {10, 20, 30}
set_two = {20, 40, 50}

set_one.difference_update(set_two)
print(set_one)


# 83- Remove items 10,20,30 from the the following set at once.

set = {10, 20, 30, 40, 50}

set.difference_update({10, 20, 30})
print(set)

print("\n")

# 84- Return a set of all unique elements in sets A & B .
set_one = {10, 20, 30, 40, 50}
set_two = {30, 40, 50, 60, 70}

print(set_one.symmetric_difference(set_two))


# 85- check if two sets have any elements in common. If yes display common elements.

set_one = {10, 20, 30, 40, 50}
set_two = {60, 70, 80, 90, 10}

if set_one.isdisjoint(set_two):
    print(" The 2 sets have no common elements.")

else:
    print("common elements are:", set_one.intersection(set_two))


# 86- update set1 by adding items from set2, except common items.

set_one = {10, 20, 30, 40, 50}
set_two = {30, 40, 50, 60, 70}

set_one.symmetric_difference_update(set_two)
print(set_one)

# 87- Remove items from set1 that are not common to both set1 and set2.
set_one = {10, 20, 30, 40, 50}
set_two = {30, 40, 50, 60, 70}

set_one.intersection_update(set_two)
print(set_one)
