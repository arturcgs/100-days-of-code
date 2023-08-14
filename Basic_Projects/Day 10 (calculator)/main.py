from art import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide (a, b):
    return a / b


def exponential(a, b):
    return a ** b


def root(a, b):
    return a ** (1/b)


def calculator():
    # printing logo
    print(logo)

    # operations dict
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide, "^": exponential, ">": root}

    # a input
    a = float(input("What's the first number? "))

    while True:
        # printing operators
        print("add: +\nsubtract: -\nmultiply: *\ndivide: /\nexponential: ^\nroot: >")

        # inputs
        operator_choice = input("Pick an operation: ")
        b = float(input("What's the next number? "))

        # result
        answer = operations[operator_choice](a, b)
        print(f"{a} {operator_choice} {b} = {answer}")

        should_continue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, "
                                f"or type 'exit' to exit.")
        if should_continue == "y":
            a = answer
        elif should_continue == "n":
            calculator()
            break
        else:
            print("Thank you for using my calculator!")
            break

# calling function
calculator()