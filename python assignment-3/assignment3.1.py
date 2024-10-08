# 1.Read the doc.txt file using Python File handling concept and return only the even length string from the file. Consider the content of doc.txt as given below:

with open('doc.txt') as file:
    for line in file.readlines():
        for word in line.split():
            if len(word)%2==0:
                print(word,end=' ')


        print()

