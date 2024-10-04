# Write a Python program to create a list of given strings individually of the list using the Python map function.

def func(n):
    return list(n)

lst = ['Red', 'Blue', 'Black', 'White', 'Pink']

res = map(func,lst)

print(list(res))

