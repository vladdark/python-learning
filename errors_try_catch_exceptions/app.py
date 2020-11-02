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


# ------------------------------------------------------------ UTIL FUNCTIONS
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid value");
