# Create a function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    return list(set(lst))

l1 = [1, 2, 2, 3, 4, 4, 5, 5]
print(unique_list(l1))