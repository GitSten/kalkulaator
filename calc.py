

def add(x,y):

    """add func"""
    return  x + y


def subtract (x, y):
    """ subtract func"""

    return x - y

def multiply(x, y):
    """multiply func"""

    return  x * y

def divide(x, y):
    """divide func"""

    return (x / y)
print("__________________")
print("|                 |")
print("|Select operation.|")
print("|1.Add            |")
print("|2.Subtract       |")
print("|3.Multiply    ️ |")
print("|4.Divide         |")
print("|                 |")
print("___________________")


while True:

    choice = input("Enter choice(1/2/3/4): ")



    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")

        if next_calculation == "no":
            break

        if next_calculation == "yes":
            print("__________________")
            print("|                 |")
            print("|Select operation.|")
            print("|1.Add            |")
            print("|2.Subtract       |")
            print("|3.Multiply    ️ |")
            print("|4.Divide         |")
            print("|                 |")
            print("___________________")

























