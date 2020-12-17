from atm_card import ATMCard

class Customer:
    atmcard = ATMCard()

    def __init__(self, id, custPin = atmcard.pin, custBalance = atmcard.balance):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def checkId(self):
        print("\nId ATM: " + str(self.id))

    def checkPin(self):
        print("Pin ATM: " + self.custPin)

    def checkBalance(self):
        print("Saldo ATM: " + str(self.custBalance))

    def withdrawBalance(self, nominal):
        self.custBalance -= nominal
        print("SISA SALDO ANDA: " + str(self.custBalance))

    def depositBalance(self, nominal):
        self.custBalance += nominal
        print("SISA SALDO ANDA: " + str(self.custBalance))
