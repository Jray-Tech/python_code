import random, string
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letters = string.ascii_lowercase
name = ''
names = ''
i = input('how long would you like the name to be?')
name_lenght = int(i)
start = 0
while start < name_lenght:
    letter = input('>').lower()
    if letter == 'l':
        name = random.choice(letters)
    elif letter == 'v':
        name = random.choice(vowels)
    elif letter == 'c':
        name = random.choice(consonants)
    else:
        name = letter
    names += name
    start = start+1
print(names)
# beautiful code
