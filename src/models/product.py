class Product:
<<<<<<< HEAD
    def __init__(self, name, price, quantity, apply_discount, check_stock, update_stock,calculate_shipping):
=======
    def __init__(self, name, price, quantity, apply_discount, check_stock, get_category,calculate_shipping):
>>>>>>> main
        self.name = name
        self.price = price
        self.quantity = quantity
        self.apply_discount = apply_discount
        self.check_stock = check_stock
<<<<<<< HEAD
        self.update_stock = update_stock
        self.calculate_shipping = calculate_shipping

=======
        self.update_stock = update_stock
        self.get_category = get_category
>>>>>>> main
        
    def get_total_price(self):
        return self.price * self.quantity
