# ------------------------------------------------------------ UTIL FUNCTIONS
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


cout_title("ERRORS | TRY | CATCH | EXCEPTIONS", breaks=0)
# managin exceptions
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value.');
