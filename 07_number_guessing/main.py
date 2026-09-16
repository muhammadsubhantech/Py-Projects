# Number Guessing Game
# Concepts: random, time, loops, conditionals, math

import random
import time
import math


def play_game():
    print("===== NUMBER GUESSING GAME =====")
    print("1. Easy   (1-20,  8 chances)")
    print("2. Medium (1-50,  6 chances)")
    print("3. Hard   (1-100, 5 chances)")

    level = input("Select level (1/2/3): ").strip()

    if level == "1":
        max_num = 20
        chances = 8
    elif level == "2":
        max_num = 50
        chances = 6
    elif level == "3":
        max_num = 100
        chances = 5
    else:
        print("Invalid choice. Easy mode start ho raha hai.")
        max_num = 20
        chances = 8

    secret = random.randint(1, max_num)
    print(f"\nMain ne 1 se {max_num} ke beech ek number socha hai.")
    print(f"Aapke paas {chances} chances hain.\n")

    start_time = time.time()   # Timer start
    attempts = 0

    while chances > 0:
        try:
            guess = int(input(f"Guess karo ({chances} left): "))
        except ValueError:
            print("❌ Sirf number daalo.")
            continue

        attempts += 1
        chances -= 1

        if guess == secret:
            end_time = time.time()
            time_taken = math.ceil(end_time - start_time)
            print(f"\n🎉 Sahi jawab! Number tha {secret}")
            print(f"Attempts: {attempts}")
            print(f"Time taken: {time_taken} seconds")
            return True

        elif guess < secret:
            print("📈 Thoda bara number socho...")
        else:
            print("📉 Thoda chhota number socho...")

        # Hint using math
        difference = abs(secret - guess)
        if difference <= 3:
            print("🔥 Bahut qareeb ho!")
        elif difference <= 10:
            print("😊 Qareeb ho.")

    print(f"\n😢 Chances khatam! Number tha → {secret}")
    return False


# Main loop
while True:
    play_game()
    again = input("\nPhir se khelna hai? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! 👋")
        break
