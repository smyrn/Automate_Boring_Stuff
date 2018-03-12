#! python3

# Regex function to duplicate the strip() method.

import re

def stripFunc(string, stripChar = None):
    if stripChar == None:
        bothStrRegex = re.compile(r'^\s*|\s*$')
        bothSpace = bothStrRegex.findall(string)
        
        if bothSpace:
            print(bothStrRegex.sub('', string))
    else:
        charRegex = re.compile(stripChar)
        print(charRegex.sub('', string))

stripFunc('  test')
stripFunc('  test    ')
stripFunc('test  ')
stripFunc('lollipop','l')

'''
while True:
    print('What is the string?')
    phrase = input()
    if phrase == '':
        break
    print('What character to strip, leave blank for whitespace?')
    arguement = input()
    stripFunc(phrase, arguement)
'''
