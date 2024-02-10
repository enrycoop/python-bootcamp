# Calculator
import __art

print(__art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operatiom_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        answer = operations[operatiom_symbol](num1, num2)
        if input(f"Type 'y to continue calculating with {answer}, or type 'n' to exit: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

    print(f"{num1} {operatiom_symbol} {num2} = {answer}")


calculator()
