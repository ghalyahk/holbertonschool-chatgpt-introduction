#!/usr/bin/python3

class Checkbook:
    """
    Class: Checkbook
    ----------------
    Simulates a simple bank checkbook to manage deposits, withdrawals, and balance inquiries.

    Attributes:
    balance (float): Current balance in the checkbook.

    Methods:
    deposit(amount): Adds money to the balance.
    withdraw(amount): Subtracts money from the balance if funds are sufficient.
    get_balance(): Prints the current balance.
    """

    def __init__(self):
        """Initialize a new checkbook with a balance of 0.0."""
        self.balance = 0.0

    def deposit(self, amount):
        """Add the specified amount to the balance and display the result."""
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Subtract the specified amount from the balance if possible."""
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Print the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """Main program loop to interact with the user."""
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
