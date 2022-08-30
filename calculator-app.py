#!/usr/bin/python3

# Locally defined functions


# Addition


def add(n1, n2):
    return n1 - n2

# subtraction


def subtraction(n1, n2):
    return n1 - n2

# multiplication


def multiply(n1, n2):
    return n1 * n2

# division


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtraction,
    "/": divide,
    "*": multiply
}

num = int(input("What is the first number?: "))
for symbol in operations:
    print(symbol)

operation_symbol = input("Pick and operation: ")
num2 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")
