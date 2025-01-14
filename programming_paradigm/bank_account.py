class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a new BankAccount instance.
        :param initial_balance: Starting balance for the account (default is 0).
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Add a specified amount to the account balance.
        :param amount: Amount to deposit.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deduct a specified amount from the account balance if sufficient funds exist.
        :param amount: Amount to withdraw.
        :return: True if withdrawal was successful, False otherwise.
        """
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Print the current account balance in a user-friendly format.
        """
        print(f"Current balance: ${self.__account_balance:.2f}")
