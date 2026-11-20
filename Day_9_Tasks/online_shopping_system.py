'''An e-commerce company organizes products using multiple levels. Create classes
Product → ElectronicProduct → MobilePhone using multilevel inheritance and
display product details.'''

class Product:
    brand = "Realme"
    price = 25000

    def display_product(self):
        print("Brand Name:",self.brand)
        print("Price:",self.price)

class ElectronicProduct(Product):
    warranty = '2 years'

    def display_electronic(self):
        print("Warranty:",self.warranty)

class MobilePhone(ElectronicProduct):
    model = "Realme 10 Pro+"
    ram = "8GB"
    storage = "128GB"

    def display_mobile(self):
        print("Model:",self.model)
        print("RAM:",self.ram)
        print("Storage:",self.storage)

m = MobilePhone()

m.display_product()
m.display_electronic()
m.display_mobile()
