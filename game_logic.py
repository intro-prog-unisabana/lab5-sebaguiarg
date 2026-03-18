from response import*
from secret_number import*
secret_number = generate_secret_number()
user = ""
count = 0
while user != secret_number:
    user = int(input("What is your guess:"))
    input_response(secret_number, user)
    count += 1

print(f"It took you {count} tries")