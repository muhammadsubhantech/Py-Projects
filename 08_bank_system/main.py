# Simple Bank Account System
# Concepts: OOP, File Handling, Loops, Conditionals, Decorators, time

import json
import os
import time
from functools import wraps


# ========== Simple Decorator ==========
def log_transaction(func):
    """Decorator jo har transaction ka time record karta hai"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"\n⏳ Processing {func.__name__}...")
        time.sleep(0.5)          # thoda real feel
        result = func(self, *args, **kwargs)
        print(f"✅ {func.__name__} completed at {time.strftime('%H:%M:%S')}")
        return result
    return wrapper


class BankAccount:
    def __init__(self, filename="account.json"):
        self.filename = filename
        self.balance = 0
        self.history = []
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.balance = data.get("balance", 0)
                self.history = data.get("history", [])
        else:
            self.balance = 0
            self.history = []

    def save(self):
        with open(self.filename, "w") as f:
            json.dump({
                "balance": self.balance,
                "history": self.history
            }, f, indent=4)

    @log_transaction
    def deposit(self, amount):
        if amount <= 0:
            print("❌ Amount 0 se bari honi chahiye.")
            return
        self.balance += amount
        self.history.append({
            "type": "Deposit",
            "amount": amount,
            "time": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save()
        print(f"💰 Rs {amount} deposit ho gaya. New Balance: Rs {self.balance}")

    @log_transaction
    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Amount 0 se bari honi chahiye.")
            return
        if amount > self.balance:
            print("❌ Insufficient balance!")
            return
        self.balance -= amount
        self.history.append({
            "type": "Withdraw",
            "amount": amount,
            "time": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save()
        print(f"💸 Rs {amount} withdraw ho gaya. New Balance: Rs {self.balance}")

    def show_balance(self):
        print(f"\n🏦 Current Balance: Rs {self.balance}")

    def show_history(self):
        if not self.history:
            print("Koi transaction nahi hui.")
            return
        print("\n----- Transaction History -----")
        for h in self.history:
            print(f"{h['time']} | {h['type']:10} | Rs {h['amount']}")


def main():
    account = BankAccount()

    while True:
        print("\n===== BANK SYSTEM =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Choice (1-5): ").strip()

        if choice == "1":
            try:
                amt = float(input("Amount: "))
                account.deposit(amt)
            except ValueError:
                print("❌ Valid number daalo.")

        elif choice == "2":
            try:
                amt = float(input("Amount: "))
                account.withdraw(amt)
            except ValueError:
                print("❌ Valid number daalo.")

        elif choice == "3":
            account.show_balance()

        elif choice == "4":
            account.show_history()

        elif choice == "5":
            print("Thank you for banking with us! 👋")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
