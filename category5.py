# 42- Arrange string characters such that lowercase letters should come first.
str = "Json"
lower = []
upper = []

for char in str:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

sorted_string = "".join(lower + upper)
print(sorted_string)


# 43- count all lower case, upper case , digits , and especial symbols from a given string.
str1 = "ge#5$2*35TW"


def find_digits_chars_symbols(str):

    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in str:
        if char.islower() or char.isupper():
            char_count += 1

        elif char.isnumeric():
            digit_count += 1

        else:
            symbol_count += 1
    print(
        f"char count is: {char_count}, digit count is: {digit_count}, symbol count is: {symbol_count}")


find_digits_chars_symbols(str1)


# 44- find all occurences of "is" in a given string ignoring the case.

string = "my cat is awesome. your cat is amazing. Is her cat asleep? "

sub_string = "is"

temp_string = string.lower()

count = temp_string.count(sub_string.lower())

print(count)


# 45- given an input string, count occurences of all characters within a string.
str = "Lemon malt"

count_dict = dict()

for char in str:
    count = str.count(char)

    # ** migim dar dictionary count_dict, key char bashe va = ba value count.**
    count_dict[char] = count

print(count_dict)


# 46- Reverse a given string.

str = "Orange"

print("original string is :", str)

str = str[::-1]

print("reversed string is :", str)


# 47- find the last position of a substring "kelly in a given string".

str = "kelly is a data scientist who knows python. kelly works at google."

index = str.rfind("kelly")
print(index)

# 48- split a given string on hyphens into several substrings and display each substring.

str = "katy_is_a_data_scientist"

sub_strings = str.split("_")

for sub in sub_strings:
    print(sub)

# 49- remove empty strings from a list of strings.
str_list = ["emma", "john", "", "kelly", None, "Eric", ""]

new_str_list = list(filter(None, str_list))
print(new_str_list)


# 50- remove all the characters other than integers from a string.

str = "I am 25 years and 10 months old."


result = "".join([item for item in str if item.isdigit()])

print(result)
