import math
def add(num1, num2):
    suma = (num1 + num2)
    return suma

def sub(num1, num2):
    resta = (num1 - num2)
    return resta

def multiply(num1, num2):
    mult = (num1 * num2)
    return mult

def divide(num1, num2):

    if num2 == 0:
        div = "Error: Division by zero is not allowed."
    else:
         div = (num1 / num2)
    return div
def exponent(base, exp):
    exp = base ** exp
    return exp
def modulo(num1, num2):
    if num2 == 0:
        res = "Error: Modulo by zero is not allowed."
    else:
        res = num1 % num2
    return res
def floor_divide(num1, num2):
    if num2 == 0:
        floor = "Error: Division by zero is not allowed."
    else:
        floor = math.floor(num1/num2)
    return floor
def absolute(num1):
    absol = math.fabs(num1)
    return absol