def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


def cout_brk(breaks=2):
    print('\n' * breaks)


def cout_title(title, breaks=2):
    title = str(title).upper()
    cout_brk(breaks)
    print(f'# ------------------------- {title}')


def cout_comment(comment, breaks=0):
    cout_brk(breaks)
    print(f'## {comment}')
