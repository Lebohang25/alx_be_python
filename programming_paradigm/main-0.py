#!/usr/bin/env python3
import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command> [amount]")
        print("Commands: deposit, withdraw, balance")
        sys.exit(1)

    command = sys.argv[1].lower()
    account = BankAccount(100)  # Starting with $100 for demonstration

    if command == "deposit":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py deposit <amount>")
            sys.exit(1)
        try:
            amount = float(sys.argv[2])
            if account.deposit(amount):
                print(f"Deposited ${amount:.2f} successfully")
            else:
                print("Invalid deposit amount")
        except ValueError:
            print("Please enter a valid number for amount")

    elif command == "withdraw":
        if len(sys.argv) != 3:
            print("Usage: python main-0.py withdraw <amount>")
            sys.exit(1)
        try:
            amount = float(sys.argv[2])
            if account.withdraw(amount):
                print(f"Withdrew ${amount:.2f} successfully")
            else:
                print("Insufficient funds or invalid amount")
        except ValueError:
            print("Please enter a valid number for amount")

    elif command == "balance":
        account.display_balance()

    else:
        print("Invalid command. Use: deposit, withdraw, or balance")

if __name__ == "__main__":
    main()
