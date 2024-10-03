# Write a program that accepts a string as input from the user and
# calculates the number of digits and letters.

res = input('Enter String:')
letters = 0
digits = 0

for i in res:
    if i>='0' and i<='9':
        digits+=1
    else:
        letters+=1

print('Aplhabets',letters)
print('Digits',digits)
