# We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must have more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.


def arrange_pile(n):
    res = []
    
    if n%2!=0:
        for i in range(n):
            if i%2==0 and i+2<n:
                res.append(i+2)
    else:
        for i in range(n):
            if i%2!=0:
                res.append(i)
    

    return res



n = int(input('Enter number:'))

print(arrange_pile(n))
