# factorial of a number

num = int(input())

res = 1

for i in range(num,1,-1):
    res*=i

print(res)