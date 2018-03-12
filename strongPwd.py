import re

def pwdCheck(pwd):
    upperRegex = re.compile(r'[A-Z]+')
    lowerRegex = re.compile(r'[a-z]+')
    digitRegex = re.compile(r'[0-9]+')

    print('Checking strength of password: ', pwd)

    while True:    
        if len(pwd) < 8:
            print('Password invalid, must be minimum of 8 characters')
            break
    
        if upperRegex.search(pwd) == None:
            print('Password invalid, must contain minimum of 1 uppercase character')
            break

        if lowerRegex.search(pwd) == None:
            print('Password invalid, must contain minimum of 1 lower character')
            break

        if digitRegex.search(pwd) == None:
            print('Password invalid, must contain minimum of 1 digit')
            break
        print('Password is strong.')
        break

while True:
    print('Please enter password, enter blank to exit:')
    password = input()

    if password == '':
        break

    pwdCheck(password)

#pwdCheck('test1'))
#pwdCheck('Test1234'))
#pwdCheck('Tester1234'))
#pwdCheck('testEr1234'))
#pwdCheck('tes1234tEr'))
