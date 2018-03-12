message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
value = {}

for character in message:
    value.setdefault(character, 0)
    value[character] = value[character] + 1

print(value)
