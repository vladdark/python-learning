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
import ecommerce.shipping
ecommerce.shipping.calc_shipping()
