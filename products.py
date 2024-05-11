class Product:

    def __init__(self, name, price, quantity):
        """
        :param name: name of product in stock or to be added to the available stuck
        :param price: Price of goods in stock
        :param quantity: quantity of goods in stock
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input. Please provide a valid input")

        self.name = str(name)
        self.price = float(price)
        self.quantity = float(quantity)
        self.active = True

    def get_quantity(self):
        # returns quantity of product
        return self.quantity

    def set_quantity(self, quantity):
        # deactivates quantity if quantity reaches zero
        if quantity <= 0:
            self.quantity = 0
            self.deactivate()
        else:
            self.quantity = quantity

    def is_active(self):
        # return true when product is active or false when not active
        return self.active

    def activate(self):
        # activates product
        self.active = True

    def deactivate(self):
        # deactivates product
        self.active = False

    def show(self):
        # return product details
        return f"{self.name}, price: {self.price}, quantity: {self.quantity}"

    def buy(self, quantity):
        # returns total price of purchase and updates the product in stock
        if not self.active:
            raise ValueError(f"{self.name} is not available for purchase")
        if quantity <= 0:
            raise ValueError("quantity should be greater than zero. ")
        if quantity > self.quantity:
            raise ValueError(f"Insufficient quantity of {self.name} available.")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price
