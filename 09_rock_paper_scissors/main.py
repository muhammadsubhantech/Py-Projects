# Rock Paper Scissors Game
# Concepts: random, loops, conditionals, OOP, time, math, decorator

import random
import time
import math
from functools import wraps


# Decorator for counting games
def count_games(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self.total_games += 1
        return func(self, *args, **kwargs)
    return wrapper


class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0
        self.total_games = 0
        self.win_streak = 0

    def get_computer_choice(self):
        return random.choice(self.choices)

    def decide_winner(self, user, computer):
        if user == computer:
            return "draw"
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            return "user"
        else:
            return "computer"

    @count_games
    def play_round(self, user_choice):
        computer = self.get_computer_choice()
        print(f"\nYou chose     : {user_choice}")
        time.sleep(0.4)
        print(f"Computer chose: {computer}")
        time.sleep(0.4)

        result = self.decide_winner(user_choice, computer)

        if result == "draw":
            print("🤝 Draw!")
            self.win_streak = 0
        elif result == "user":
            print("🎉 You Win!")
            self.user_score += 1
            self.win_streak += 1
        else:
            print("😢 Computer Wins!")
            self.computer_score += 1
            self.win_streak = 0

        print(f"Score → You: {self.user_score} | Computer: {self.computer_score}")
        if self.win_streak >= 3:
            print(f"🔥 Win Streak: {self.win_streak}!")

    def show_stats(self):
        print("\n===== GAME STATS =====")
        print(f"Total Games   : {self.total_games}")
        print(f"Your Score    : {self.user_score}")
        print(f"Computer Score: {self.computer_score}")

        if self.total_games > 0:
            win_percent = math.floor((self.user_score / self.total_games) * 100)
            print(f"Win Rate      : {win_percent}%")
        else:
            print("Win Rate      : 0%")


def main():
    game = RockPaperScissors()

    print("===== ROCK PAPER SCISSORS =====")
    print("Type: rock / paper / scissors")
    print("Type 'stats' to see score")
    print("Type 'quit' to exit\n")

    while True:
        user_input = input("Your choice: ").strip().lower()

        if user_input == "quit":
            game.show_stats()
            print("Thanks for playing! 👋")
            break

        elif user_input == "stats":
            game.show_stats()

        elif user_input in game.choices:
            game.play_round(user_input)

        else:
            print("❌ Invalid choice. rock / paper / scissors likho.")


if __name__ == "__main__":
    main()
