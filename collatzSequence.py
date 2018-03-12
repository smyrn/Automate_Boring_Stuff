#Create the Collatz function.
def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

#Take user input and run Collatz function on it until it reaches 1.

while True:
    try:
        print('Enter number:')
        n = int(input())

    except ValueError:
        print('You must enter an integer')
        continue

    while n != 1:
        n = collatz(n)
        print(n)
