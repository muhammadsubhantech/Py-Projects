# Strong Password Generator
# Student Level Pure Python Project

import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    characters = string.ascii_letters  # a-z A-Z

    if use_digits:
        characters += string.digits     # 0-9
    if use_symbols:
        characters += string.punctuation  # !@#$%^&* etc.

    if length < 4:
        print("❌ Password length should be at least 4.")
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password


print("===== PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("\nEnter password length (e.g. 12): "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    digits = input("Include numbers? (y/n): ").lower() == "y"
    symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, digits, symbols)

    if password:
        print("\n🔐 Your Password:", password)
        print("Copy it and store safely!")

    again = input("\nGenerate another? (y/n): ").lower()
    if again != "y":
        print("Thank you! Stay safe 🔒")
        break
