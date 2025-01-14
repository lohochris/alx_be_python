class BankAccount:
    """
    A class representing a simple bank account.
    """

    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount with an optional initial balance.
        :param initial_balance: The starting balance of the account (default is 0).
        """
        self._account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        :param amount: The amount to deposit.
        """
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if sufficient funds are available.
        :param amount: The amount to withdraw.
        :return: True if withdrawal is successful, False otherwise.
        """
        if amount > self._account_balance:
            return False
        elif amount > 0:
            self._account_balance -= amount
            return True
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Display the current account balance.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")
