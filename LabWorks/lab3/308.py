import sys

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return int(self.balance) if self.balance.is_integer() else self.balance

def solve():
    # Считываем данные
    data = sys.stdin.read().split()
    if len(data) < 2:
        return

    initial_balance = int(data[0])
    withdrawal_amount = int(data[1])

    # Создаем аккаунт (владельца назовем просто 'User')
    acc = Account("User", initial_balance)
    
    # Пытаемся снять деньги и выводим результат
    result = acc.withdraw(withdrawal_amount)
    print(result)

if __name__ == "__main__":
    solve()