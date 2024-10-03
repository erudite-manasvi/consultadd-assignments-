# Write a Python program to check if a number is a power of two using recursion.

def isPower(n):
    if n==1: return True
    elif n<=0 or n%2!=0: return False

    return isPower(n//2)

n = int(input('Enter Number:'))

if isPower(n):
    print(f'{n} is power of 2')
else:
    print(f'{n} is not a power of 2')

    