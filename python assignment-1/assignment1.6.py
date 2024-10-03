# Perfect Number

num = int(input('Enter number:'))

sum = 0
if num % 2 !=0: 
    print('Not a perfect number')

else:
    for i in range(1,num//2+1):
        if num%i==0: sum+=i
    print('Perfect Number') if sum==num else print('Not a perfect number') 
