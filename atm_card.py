class ATMCard:
    def __init__(self, defaultPin = "1234", defaultBalance = 10000):
        self.pin = defaultPin
        self.balance = defaultBalance

    def checkPin(self):
        print("Pin ATM: " + self.pin)

    def checkBalance(self):
        print("Saldo ATM: " + str(self.balance))
