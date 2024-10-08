# Write a program to count the lines in a file “demo.txt”

with open('doc.txt') as file:
    print(len(file.readlines()))