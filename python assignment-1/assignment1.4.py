# Write a Python program to find the sum of all odd numbers between two given numbers.

num1 = int(input())
num2 = int(input())

sum=0

for i in range(num1,num2):
    if(i%2!=0):
        sum+=i

print(sum)


