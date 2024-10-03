#Write a Python program to calculate the sum of digits of a given number until the sum becomes a single-digit number.
num = int(input('Enter number:'))
res = 0

while(num>0 or res>9):
    if num == 0:
        num = res
        res = 0
        
    res+=num%10
    num//=10
 
print(res)