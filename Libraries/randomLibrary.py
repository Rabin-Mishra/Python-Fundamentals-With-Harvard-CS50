# use of random library and its different modules like choice(seq), randint(x), and shuffle(x)
# two ways of importing
# import random(first way)
# from random import choice(second way)

import random

coin = random.choice(['Heads', 'Tails'])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ['queen', 'king', 'jack']
random.shuffle(cards)
print(cards)
for card in cards:
    print(card)
