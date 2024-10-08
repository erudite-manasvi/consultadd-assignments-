# Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should map the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension.

def map_list_to_dict(l1,l2):
    if len(l1)!=len(l2):
        return "Mapping can't be done"
    
    res =  zip(l1, l2)

    return dict(res)

def map_list_to_dict2(l1,l2):
    if len(l1)!=len(l2):
        return "Mapping can't be done"
    
    res =  {l1[i]:l2[i] for i in range(len(l1))}

    return res
    
l1 = ['Sam', 'Alice', 'Mona']
l2 = ['Commerce', 'Science', 'Computer']

print(map_list_to_dict2(l1,l2))