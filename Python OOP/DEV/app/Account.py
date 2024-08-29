class Account:
    def __init__(self, owner, number, balance):
        self._owner = owner
        self._number = number
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            print("The balance cannot be negative")
        else:
            self._balance = balance