#LCM and GCD of a number
def lcmAndGcd(A , B):
    a, b = A, B
    while (a > 0 and b > 0):
        if a > b:
            a = a % b
        else:
            b = b % a
    
        res = [0, 0]
    if a == 0:
        res[1] = b
    else:
        res[1] = a
    
    res[0] = (A * B) // res[1]
    return res

print(lcmAndGcd(12,18))