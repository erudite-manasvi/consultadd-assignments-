# Write a Python program to input marks for five subjects Physics, Chemistry, Biology, Mathematics, and Computer. Calculate the
# percentage and grade according to the following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F

subjects = ['Physics', 'Chemistry', 'Biology', 'Mathematics','Computer']

sum = 0

for i in subjects:
    marks = int(input('Enter marks of'+' '+i+':'))
    sum+=marks

res = (sum/500)*100

print(res)

if res>=90:
    print('Grade A')
elif res>=80 and res<90:
    print('Grade B')
elif res>=70 and res<80:
    print('Grade C')
elif res>=60 and res<70:
    print('Grade D')
elif res>=40 and res<60:
    print('Grade E')
else:
    print('Grade F')