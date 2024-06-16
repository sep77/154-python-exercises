# 67- convert the below lists into a dictionary.
keys = ["ten", "twenty", "thirty"]

values = [10, 20, 30]

result_dict = dict(zip(keys, values))
print(result_dict)

print("\n")

# 68- merge the following dictionaries into one.

dict1 = {"ten": 10, "twenty": 20, "thirty": 30}
dict2 = {"thirty": 30, "fourty": 40, "fifty": 50}

dict3 = {**dict1, **dict2}
print(dict3)

print("\n")

# 69- Access the value of key "history" from the below dict.

sampleDict = {
    "class": {
        "student": {
            "name": "mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

value = sampleDict["class"]["student"]["marks"]["history"]
print(value)

print("\n")

# 70- Initialize dictionary with default values

employees = ["kelly", "emma", "john"]

defaults = {"Designation": "Application Developer", "salary": 8000}

result_dict = dict.fromkeys(employees, defaults)
print(result_dict["emma"])

print("\n")

# 71- create a new dictionary by extracting the following keys from a below dictionary.

sampleDict = {
    "name": "kelly",
    "age": "25",
    "salary": 8000,
    "city": "newyork"
}

# 72- keys to extract

keys = ["name", "salary"]

# first way
new_dict = {k: sampleDict[k] for k in keys}
print(new_dict)

# second way
extract_keys = {k: v for (k, v) in sampleDict.items() if k in keys}
print(extract_keys)
print("\n")

# 73- Delete set of keys from a dictionary.
sampleDict = {
    "name": "kelly",
    "age": "25",
    "salary": 8000,
    "city": "newyork"
}

# 74- keys to remove
keysToRemove = ["name", "salary"]

new_dict = {k: sampleDict[k] for k in sampleDict.keys() - keysToRemove}
print(new_dict)


# 75- check if a value 200 exists.

sample_Dictt = {'a': 100, 'b': 200, 'c': 300}

print(200 in sample_Dictt.values())


# 76- Rename key city to location in the following dictionary.
sampleDict = {
    "name": "kelly",
    "age": "25",
    "salary": 8000,
    "city": "newyork"
}


sampleDict["location"] = sampleDict.pop("city")
print(sampleDict)

print("\n")

# 77- Get the key of a minimum value from the following dictionary.

sampleDict = {
    "physics": 82,
    "math": 64,
    "history": 75
}

print(min(sampleDict, key=sampleDict.get))

print("\n")

# 78- change emily's salary to 8500 in the below dictionary.

sampleDict = {
    "emp1": {"name": "john", "salary": 7500},
    "emp2": {"name": "jane", "salary": 8000},
    "emp3": {"name": "emily", "salary": 6000},
}

sampleDict["emp3"]["salary"] = 8500
print(sampleDict)
