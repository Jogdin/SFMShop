class Product:
    def __init__(self, name, price, quantity, apply_discount, check_stock, update_stock,calculate_shipping):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.apply_discount = apply_discount
        self.check_stock = check_stock
        self.update_stock = update_stock
        self.calculate_shipping = calculate_shipping

        
    def get_total_price(self):
        return self.price * self.quantity
