# Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password and if the password is incorrect give a chance to enter it again but it should not be more than 3 times.

#- contains one upper, lower case, special symbol, digits, minimum 6 len

def containsUpperCase(password):
    for ch in password:
        if ch.isupper():return True
    
    return False

def containsLowerCase(password):
    for ch in password:
        if ch.islower():return True
    
    return False

def containsSpecialChar(password):
    for ch in password:
        if not (ch.isalpha() or ch.isdigit() or ch==' '):
            return True
        
    return False

def containsDigit(password):
    for ch in password:
        if ch.isdigit():return True

    return False

def isValid(password):
    return password.strip() and containsDigit(password) and containsUpperCase(password) and containsLowerCase(password) and containsSpecialChar(password) and len(password)>=6



def main():
    max_attempts = 3
    c = 1
    
    while c <= max_attempts:
        password = input(f'Enter password: ')
        if isValid(password):
            print("Password is valid!")
            break
        else:
            print('Password must contain one upper, lower case, special symbol, digit &  minimum of 6 length')
            c += 1


if __name__=='__main__':
    main()