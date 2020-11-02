def cout_brk(breaks=2):
    print('\n' * breaks)


def cout_title(title, breaks=2):
    title = str(title).upper()
    cout_brk(breaks)
    print(f'---------------------------------------------- {title}')


def cout_comment(comment, breaks=0):
    comment = str(comment).upper()
    cout_brk(breaks)
    print(f'## {comment}')


cout_title('PARAMETERS')


def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard!")


def calc_cost(discount, total, shipping):
    print(f'total: {total}, shipping: {shipping}, discount: {discount}')


print("Start")
greet_user('John', "Smith")
calc_cost(total=50, shipping=5, discount=0.1)
print("Finish")

cout_title('RETURNS')


def square(number):
    return number * number


print(f'square of 3: {square(3)}')

cout_title('EXERCISE: EMOJI TO FUNCTIONS')
cout_comment('My Solution')

messages = [
    "Good morning :)",
    "Good morning sunshine",
    "I feel sad :("
]


def detect_emoji(message):
    emojis = {
        ':)': "🙂",
        ':(': "☹",
        ':D': "😁",
    }

    words = message.split(' ')
    output = ''
    for word in words:
        output += emojis.get(word, word) + " "
    print(output)


for message in messages:
    detect_emoji(message)

cout_comment('Mosh Solution')


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ':)': "🙂",
        ':(': "☹",
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + " "
    return output


for message in messages:
    print(emoji_converter(message))
