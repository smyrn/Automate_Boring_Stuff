import re

senRegex = re.compile(r'''(
(alice|bob|carol)          # Names
\s                         # 1 space character
(eats|pets|throws)         # Actions
\s                         # 1 space character
(apples|cats|baseballs)    # Stuff
\.
)''', re.VERBOSE | re.IGNORECASE)


print(senRegex.search('Alice eats apples.').group())
print(senRegex.search('Bob pets cats.').group())
print(senRegex.search('Carol throws baseballs.').group())
print(senRegex.search('Alice throws Apples.').group())
print(senRegex.search('BOB EATS CATS.').group())
print()
#print(senRegex.search('Robocop eats apples.').group())
#print(senRegex.search('ALICE THROWS FOOTBALLS.').group())
#print(senRegex.search('Carol eats 7 cats.').group())
