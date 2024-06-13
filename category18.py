# 150- write a program that takes a string and checks if it is a palindrome.
# A palindrome is a string that reads the same, whether forward or backward.

import math
import random
word = input("Enter a word:").lower()

rev_word = reversed(word)

if list(rev_word) == list(word):
    print("It is a palindrome.")
else:
    print("It is NOT a palindrome.")


# 151- write a program that takes a sentence, sorts the words alphabetically and return them.

string = input("Enter a sentence:")

words = [word.lower() for word in string.split()]

words.sort()
print("The sorted words are:")

for word in words:
    print(word)


# 152- write a program that performs set operations such as union,intersection,difference
# and symmetric difference on the following two sets.

set_a = {0, 1, 2, 3, 4, 5}
set_b = {11, 12, 13, 14, 15, 16}

# union
print("Union of set A and B:", set_a | set_b)

# intersection
print("intersection:", set_a & set_b)

# difference:
print("difference:", set_a - set_b)

# symmetric difference
print("symmetric difference:", set_a ^ set_b)


# 153-  write a program that removes the punctuations from the following string and prints the results.

string = """
Hi !!!
welcome I guess, ?
2>1
[0-9]
{2,4}
\t
\n
my_email@my_email.com
"""
punctuations = r"""[],(),?,\,@,.,>,!,{}"""

string_result = ""

for char in string:
    if char not in punctuations:
        string_result += char

print(string_result)


# 154- write a program that takes a string input from the user and counts how many times each of
# the five vowel characters have been repeated in the string and returns the result.

string = input("Enter a word/sentence:").lower()

vowels = "aeiou"
count = {}.fromkeys(vowels, 0)

for char in string:
    if char in count:
        count[char] += 1
print(count)
