import re

alphaRegex = re.compile(r'''(
[A-Z]          # 1 capital letter
[a-z]+         # 1 or more lower case letters
\s             # 1 space character
Nakamoto       # Nakamoto
)''', re.VERBOSE)

print(alphaRegex.search('Satoshi Nakamoto').group())
print(alphaRegex.search('Alice Nakamoto').group())
print(alphaRegex.search('Robocop Nakamoto').group())
print()
#print(alphaRegex.search('satoshi Nakamoto').group())
#print(alphaRegex.search('Mr. Nakamoto').group())
#print(alphaRegex.search('Nakamoto').group())
#print(alphaRegex.search('Satoshi nakamoto').group())
