import random
import logging
logging.basicConfig(filename='coinTossDebug.log', level=logging.DEBUG,
                    format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
logging.debug('Variable guess is set as: ' + str(guess))

randInt = random.randint(0, 1)
if randInt == 0:
    toss = 'tails'
else:
    toss = 'heads'
logging.debug('Variable toss is set as: ' + str(toss))

if toss == guess:
    logging.debug(str(toss) + ' = ' + str(guess) + ' are equal')
    print('You got it!')
else:
    logging.debug(str(toss) + ' != ' + str(guess) + ' so they are not equal')
    print('Nope! Guess again!')
    guess = input()
    logging.debug('Variable guess is set as: ' + str(guess))
    if toss == guess:
        logging.debug(str(toss) + ' = ' + str(guess) + ' are equal')
        print('You got it!')
    else:
        logging.debug(str(toss) + ' != ' + str(guess) + ' so they are not equal')
        print('Nope. You are really bad at this game.')

logging.debug('End of program')
