#Whether a number is Anagram or Not

s1 = "listen"
s2 = "slient"

print('Anagram') if sorted(s1)==sorted(s2) else print('Not Anagram')

#or
# from collections import Counter

# print('Anagram') if Counter(s1)==Counter(s2) else print('Not Anagram')