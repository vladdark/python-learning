import converters
import utils
from converters import kg_to_lbs
from utils import find_max, cout_brk, cout_title, cout_comment

cout_title('USING CONVERTERS MODULE')

print(kg_to_lbs(100))
print(kg_to_lbs(70))

print(converters.kg_to_lbs(70))

cout_title('USING UTILS FUNCTIONS')

numbers = [3, 6, 2, 8, 4, 10]
print(f'array of numbers: {numbers}')
print(f'Max number is: {max(numbers)}')
print(f'Max number is: {find_max(numbers)}')
print(f'Max number is: {utils.find_max(numbers)}')

cout_title('USING ECOMMERCE MODULE')
# import ecommerce
# from ecommerce import shipping
from ecommerce.shipping import calc_shipping

# ecommerce.shipping.calc_shipping()


calc_shipping()
calc_shipping()
calc_shipping()

cout_title('GENERATING RANDOM NUMBERS')
import random

cout_comment('generating random numbers (float)')
for i in range(3):
    print(random.random())

cout_comment('generating random numbers (int)')
for i in range(3):
    print(random.randint(10, 20))

cout_comment('get random names from array')
members = ['John', 'Mary', 'Bob', 'Mosh']
for i in range(3):
    print(random.choice(members))

cout_title('EXERCISE: ROLLING DICES')

cout_comment('My Solution')


class MyDice:
    def roll(self):
        return random.randint(1, 6), random.randint(1, 6)


dice = MyDice()
print(f'Result of rolling dices: {dice.roll()}')

cout_comment('Mosh Solution')


class MoshDice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = MoshDice()
print(dice.roll())

cout_title('PYTHON MODULES: PATH')
from pathlib import Path

# Absolute path
# windows: c:\Program Files\Microsoft
# mac: /usr/local/bin
# Relative path
cout_comment("'ecommerce' path exist")
path = Path("ecommerce")
print(path.exists())

cout_comment("'ecommerce1' path doesn't exist")
path = Path("ecommerce1")
print(path.exists())

cout_comment("creating and deleteing 'emails' folder")
path = Path("emails")
print(path.exists())
# path.mkdir()  # uncomment if you want to create the directory
# path.rmdir()  # uncomment if you want to remove the directory
print(path.exists())

cout_comment("finding all files and directories in a path")
path = Path()
print(path.glob('*.*'))  # all files
print(path.glob('*.py'))  # all python files

cout_comment('listing all python files')
for file in path.glob('*.py'):
    print(file)

cout_comment('listing all files and directories')
for element in path.glob('*'):
    print(element)
