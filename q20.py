import re

numRegex = re.compile(r'^\d{1,3}(,\d{3})*$')

print(numRegex.search('42').group())
print(numRegex.search('1,234').group())
print(numRegex.search('6,368,745').group())
print()
#print(numRegex.search('12,34,567').group())
#print(numRegex.search('1234').group())
