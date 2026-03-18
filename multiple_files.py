from utils import *
mensaje = input("Please type your message\n")
reves = flip(mensaje)
cuenta = count_letters(mensaje,"a")
print(f"Your encoded message is: {reves}{cuenta}")