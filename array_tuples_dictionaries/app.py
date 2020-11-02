print('----------------------------------------------------------------- NAMES')
names = ['John', 'Bob', 'Mosh', 'Sara', 'Maj', 'Rudolf']

print(names)
print(names[-2])
print(names[2:])
print(names[2:4])
print(names[2:-2])

# changing name by index
names[0] = 'Jon'
print(names)

print('\n\n\n----------------------------------------------------------------- FINDIND LARGER NUMBER')
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number

print("Finding larger number")
print(numbers)
print(max)

print('\n\n\n----------------------------------------------------------------- LARGER NUMBER')
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number

print("Finding larger number")
print(numbers)
print(max)

print('\n\n\n----------------------------------------------------------------- MATRIX')
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix)
print(matrix[0][1])
print('\n')
print('printing each element')
for row in matrix:
    for item in row:
        print(item)

print('\n\n\n----------------------------------------------------------------- NUMBERS')
numbers = [5, 2, 1, 7, 4]

print('\n## appending item 20')
numbers.append(20)
print(numbers)

print('\n## inserting a new item (10) at the beginning')
numbers.insert(0, 10)
print(numbers)

print('\n## deleting item 10')
numbers.remove(10)
print(numbers)

print('\n## clearing array_tuples_dictionaries')
numbers.clear()
print(numbers)

print('\n## reassigning values')
numbers = [5, 2, 1, 7, 4]
print(numbers)

print('\n## index of 5')
print(numbers.index(5))

print('\n## checking the existence of a number')
print(f"It's 50 in the list: {50 in numbers}")

print('\n## copying the list')
numbers_copy = numbers.copy()
numbers_copy.append(10)
print(numbers)
print(numbers_copy)

print('\n## sorting the list')
numbers_sorted = numbers.copy()
numbers_sorted.sort()
print(numbers)
print(numbers_sorted)

print('\n## reverting the list')
numbers_reversed = numbers.copy()
numbers_reversed.reverse()
print(numbers)
print(numbers_reversed)

print('\n## printing x for each value in the array_tuples_dictionaries')
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

print(numbers)

print('\n\n\n----------------------------------------------------------------- EXERCISE: REMOVING DUPLICATES')
numbers = [5, 6, 7, 8, 9, 1, 2, 2, 5, 4, 6, 3, 1, 2, 2, 4, 4, 3, 10, 12, 11, 11, 10, 15]
numbers_no_duplicates = []

print('\n## My solution')
for number in numbers:
    if not (number in numbers_no_duplicates):
        numbers_no_duplicates.append(number)

print(f'Original     : {numbers}')
print(f'No Duplicates: {numbers_no_duplicates}')

print('\n## Mosh solution')
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(f'Original     : {numbers}')
print(f'No Duplicates: {uniques}')
print('\n## Almost equal! Yahooo!!!')

print('\n\n\n----------------------------------------------------------------- TUPLES')
print('# tuples are inmutable | can not be changed')
numbers_tuples = (1, 2, 3)
print(f'tuple: {numbers_tuples}')
print(f'first item: {numbers_tuples[0]}')

print('\n\n\n----------------------------------------------------------------- UNPACKING')
coordinates = (1, 2, 3)
result = coordinates[0] * coordinates[1] * coordinates[2]

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
result = x * y * z

x, y, z = coordinates
result = x * y * z

print(f'Unpackaging tuple: {coordinates} into variables x, y, z')
print(f'x: {x} | y: {y} | z: {z}')

print('\n\n\n----------------------------------------------------------------- DICTIONARIES')
print('We use dictionaries when we need a structure to store data in the form of key => value')
print('Keys needs to be uniques')
customer = {
    "name": "John Smith",
    "age": "30",
    "is_verified": True
}
print(customer)
print(f"customer name: {customer['name']}")
print(f"customer's birthday: {customer.get('birthday')}")
print(f"customer's birthday with default: {customer.get('birthday', 'Jan 1st 1980')}")

print('\n\n\n----------------------------------------------------------------- EXERCISE: PRINT NUMBERS NAMES')
# phone_number = input("Please give us your phone number > ")

print('\n## My solution')
phone_number = '503 8919 3489'
number_names = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}
print(f"Your phone number: {phone_number}")
phone_number_name = ''
for char in phone_number:
    if char == ' ':
        continue
    phone_number_name += number_names.get(char, "") + " "
print(phone_number_name)

print('\n## Mosh solution')
phone = '503 5683 8919'
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}
print(f"Your phone number: {phone}")
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
print('\n## Almost equal. Good')

print('\n\n\n----------------------------------------------------------------- EMOJI DICTIONARY')
# message = input("> ")
messages = [
    "Good morning :)",
    "Good morning sunshine",
    "I feel sad :("
]

emojis = {
    ':)': "🙂",
    ':(': "☹",
    ':D': "😁",
}

print(messages)
print(emojis)

for message in messages:
    words = message.split(' ')
    output = ''
    for word in words:
        output += emojis.get(word, word) + " "
    print(output)
