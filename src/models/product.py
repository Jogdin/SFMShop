class Product:
    def __init__(self, name, price, quantity, apply_discount, check_stock, get_category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.apply_discount = apply_discount
        self.check_stock = check_stock
        self.get_category = get_category
        
    def get_total_price(self):
        return self.price * self.quantity
