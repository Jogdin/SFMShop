class User:
    def __init__(self, name, email,adress):
        self.name = name
        self.email = email
        self.adress = adress
    def get_info(self):
        return "Пользователь: " + self.name + ", Email: " + self.email
