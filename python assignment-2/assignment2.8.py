# Write a Python function that counts the number of vowels in a given string.

vowels_list = ['a','e','i','o','u']

def count_vowels(string):
    c=0
    for s in string:
        if s.lower() in vowels_list:
            print(s.lower())
            c+=1

    return c

print(count_vowels("Hello my FRIENDS"))
