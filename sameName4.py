eggs = 'global'

def spam():
    global eggs
    #print(eggs) #error
    eggs = 'spam local'

spam()
print(eggs)
