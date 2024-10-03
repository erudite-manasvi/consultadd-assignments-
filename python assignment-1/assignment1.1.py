"""If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “Python Training” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string."""

num = int(input('Enter number:'))

if num%3==0 and num%5==0:
    print('Consultadd - Python Training')
elif num%3==0:
    print('Consultadd')
elif num%5==0:
    print('Python Training')
else:
    print('Neither divisible by 3 nor by 5')