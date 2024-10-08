# Aditi has used text editing software to type some text. After saving the article as words.txt, she realized that she had wrongly typed the alphabet “J" instead of “I" everywhere in the article. Write a function definition for JtoI() in Python that would display the corrected version of the entire content of the file WORDS.TXT with all the alphabet "J" to be displayed as an alphabet "I" on the screen. Note: Assume that words.txt does not contain any J alphabet otherwise.

def JtoI(file):
    res = list(file.read())
    for i in range(len(res)):
        if res[i]=='j':
            res[i]='i'
        elif res[i]=='J':
            res[i]='I'
            
    return ''.join(res)

with open('words.txt') as file:
    print(JtoI(file))