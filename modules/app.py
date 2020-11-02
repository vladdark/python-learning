import converters
import utils
from converters import kg_to_lbs
from utils import find_max

# ------------------------------------ USING CONVERTERS MODULE
print(kg_to_lbs(100))
print(kg_to_lbs(70))

print(converters.kg_to_lbs(70))

# ------------------------------------ USING UTILS FUNCTIONS
numbers = [3, 6, 2, 8, 4, 10]
print(f'array of numbers: {numbers}')
print(f'Max number is: {max(numbers)}')
print(f'Max number is: {find_max(numbers)}')
print(f'Max number is: {utils.find_max(numbers)}')

# ------------------------------------ USING ECOMMERCE MODULE
# import ecommerce
# from ecommerce import shipping
from ecommerce.shipping import calc_shipping

# ecommerce.shipping.calc_shipping()


calc_shipping()
calc_shipping()
calc_shipping()

# ------------------------------------ GENERATING RANDOM NUMBERS
import random

print('\n generating random numbers (float)')
for i in range(3):
    print(random.random())

print('\n generating random numbers (int)')
for i in range(3):
    print(random.randint(10, 20))

print('\n get random names from array')
members = ['John', 'Mary', 'Bob', 'Mosh']
for i in range(3):
    print(random.choice(members))


# ------------------------------------ EXERCISE: ROLLING DICES
print('\nEXERCISE: ROLING DICES')
print('\nMy Solution')


class MyDice:
    def roll(self):
        return random.randint(1, 6), random.randint(1, 6)


dice = MyDice()
print(f'\nResult of rolling dices: {dice.roll()}')

print('\nMosh Solution')


class MoshDice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = MoshDice()
print(dice.roll())

