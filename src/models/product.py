class Product:
    def __init__(self, name, price, quantity, apply_discount):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.apply_discount = apply_discount
        
    def get_total_price(self):
        return self.price * self.quantity
