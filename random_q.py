import random

seed = int(input("Enter a seed number:"))
random.seed(seed)

def generate_secret_number(start=1, end=100):
    entero_aleatorio = random.randint(start, end)
    return entero_aleatorio