# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
l1 = [1,2,3]

idx = int(input('Enter Index Value:- '))

try:
    print(f'Element over index {idx} is:- {l1[idx]}')
except IndexError as e:
    print(f'{idx} - {e} exception')