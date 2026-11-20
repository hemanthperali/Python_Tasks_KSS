'''An online store supports multiple payment methods: CreditCard, UPI, and
NetBanking. Create a base class Payment with a method process_payment() and
override it in each payment type.'''

class Payment:
    def process_payment(self):
        print("Processing payment")

class CreditCard(Payment):
    def process_payment(self):
        print("Payment through CreditCard")

class UPI(Payment):
    def process_payment(self):
        print("Payment through UPI")

class NetBanking(Payment):
    def process_payment(self):
        print("Payment through Netbanking")


c = CreditCard()
u = UPI()
n = NetBanking()

c.process_payment()
u.process_payment()
n.process_payment()
      