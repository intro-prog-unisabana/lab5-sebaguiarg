import os
import math

directory = os.getcwd()
print(f"Current working directory: {directory}")

num = int(input("Enter an integer:"))

def operacion_log (num):
    resultado = math.log2(num)
    ceiling = math.ceil(resultado)
    floor = math.floor(resultado)
    return resultado

def operacion_ceiling (num):
    resultado = math.log2(num)
    ceiling = math.ceil(resultado)
    floor = math.floor(resultado)
    return ceiling

def operacion_floor (num):
    resultado = math.log2(num)
    ceiling = math.ceil(resultado)
    floor = math.floor(resultado)
    return floor

result_log = operacion_log(num)
result_ceiling = operacion_ceiling(num)
result_floor = operacion_floor(num)
print(f"Log base 2 of {num} is: {result_log}")
print(f"Floor: {result_floor}")
print(f"Ceiling: {result_ceiling}")