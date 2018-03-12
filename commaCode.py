def commaConvert(listValue):
    x = ''
    for i in range(0, (len(listValue) - 1)):
        x = x + str(listValue[i]) + ', '
    x = x + 'and ' + str(listValue[(len(listValue) - 1)])
    print(x)

spam = ['apples', 'bananas', 'tofu', 'cats']
commaConvert(spam)

slick = ['apples', 'bananas', 'tofu', 'cats', 'fish', 'peanuts']
commaConvert(slick)

small = ['apples', 'bananas']
commaConvert(small)
