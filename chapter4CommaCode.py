def comma(listVariable):
    for i in range(0,(len(listVariable) - 1)):
        string = string + listVariable[(i)] + ', '
        #print(listVariable[(i)] + ', ')
        
    

spam = ['apples', 'bananas', 'tofu', 'cats']
eggs = ['apples', 'bananas', 'tofu']

print('Printing spam')
comma(spam)

print('Pringing eggs')
comma(eggs)
