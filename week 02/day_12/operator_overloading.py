## 9. Micro Challenge: Operator Overloading.

## Goal: Allow adding two wallets: w1 + w2.


class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount


w1 = Wallet(50)
w2 = Wallet(30)

print(w1 + w2)
