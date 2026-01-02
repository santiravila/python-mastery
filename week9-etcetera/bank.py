class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()
    

"""

balance = 0


def main():
    print(balance)
    deposit(100)
    withdraw(50)
    print(balance)


def deposit(n):
    global balance
    balace += 1


def withdraw(n):
    global balance
    balace -= 1


if __name__ == "__main__":
    main()
"""