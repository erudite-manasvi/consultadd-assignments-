#Write a Python program to reverse a number using a while loop.

num = int(input('Enter Number:'))

res = 0

while(num>0):
    digi=num%10
    res=res*10+digi
    num//=10

print(res)
