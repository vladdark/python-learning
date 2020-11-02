class Point:
    # constructor in python
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('moved')

    def draw(self):
        print('draw')


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()


# point2 = Point()
# point2.x = 1
# print(point2.x)


point = Point(10, 20)
print(point.x)
point.x = 11
print(point.x)


# ---------------------------------------- EXERCISE: CREATING PERSON CLASS
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} is talking...")


person = Person('Rodolfo')
person.talk()

john = Person('John Smith')
john.talk()
