import click

def add(x,y):

    """add func"""
    return  (x + y)


def subtract (x, y):
    """ subtract func"""

    return (x - y)

def multiply(x, y):
    """multiply func"""

    return (x * y)

def divide(x, y):
    """divide func"""

    return (x / y)

def square_root(x):
    """square root func"""

    return(x ** 0.5)

def root(x):
    return(x * x )


print("|___Calc ver 1.0____|")
print(" Built by Sten Sagar ")
print("| ---------------   |")
print("|Select operation.  |")
print("|1.Add         +    |")
print("|2.Subtract    -    |")
print("|3.Multiply    *    |")
print("|4.Divide      /    |")
print("|5.Square root √    |")
print("|6.Root        x²   |")
print("___________________")


while True:

    choice = input("Enter choice(1/2/3/4/5/6): ")




    if choice in ('1', '2', '3', '4',):
        num1 = click.prompt('Please enter first number', type=float)
        num2 = click.prompt('Please enter second number', type=float)




        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))




    else:
        if choice in "5,6":
            num1 = click.prompt('Please enter number', type=float)

        if choice =="5":
            print("√",num1,"=",square_root(num1))

        if choice == "6":
            print(num1,"x²","=",root(num1))


        next_calculation = input("Let's do next calculation? (yes/no): ")

        if next_calculation == "no":
            break

        if next_calculation == "yes":
            print("|___Calc ver 1.0____|")
            print(" Built by Sten Sagar ")
            print("| ---------------   |")
            print("|Select operation.  |")
            print("|1.Add         +    |")
            print("|2.Subtract    -    |")
            print("|3.Multiply    *    |")
            print("|4.Divide      /    |")
            print("|5.Square root √    |")
            print("|6.Root        x²   |")
            print("___________________")



