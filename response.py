from secret_number import *

def input_response(secret_number, user_input):
    if user_input > secret_number:
        print("Too high! Try a lower number.")
    elif user_input < secret_number:
        print("Too low! Try a higher number.")
    elif user_input == secret_number:
        print("Correct! You guessed the number!")