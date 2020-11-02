def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard!")


def calc_cost(total, shipping, discount):
    print(f'total: {total}, shipping: {shipping}, discount: {discount}')


print("Start")
greet_user('John', "Smith")
calc_cost(total=50, shipping=5, discount=0.1)
print("Finish")
