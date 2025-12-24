class Product:
    total_products_sold = 0
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def sell_product(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            Product.total_products_sold += amount
            print(f"Sold {amount} of {self.name}.")
        else:
            print(f"Insufficient quantity of {self.name} to sell {amount}.")
    @classmethod
    def get_total_products_sold(cls):
        return cls.total_products_sold

product1 = Product("Laptop", 1000, 50)
product2 = Product("Smartphone", 500, 100)
product1.sell_product(5)
product2.sell_product(10)
print("Total products sold:", Product.get_total_products_sold())
product1.sell_product(60)  # Attempt to sell more than available quantity
