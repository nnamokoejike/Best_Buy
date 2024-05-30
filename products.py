class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None

    def show(self):
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promotion_info}"

    def set_promotion(self, promotion):
        self.promotion = promotion

    def buy(self, quantity):
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def get_quantity(self):
        return self.quantity

    def is_active(self):
        return self.quantity > 0


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def is_active(self):
        return True


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of {self.name}")
        return super().buy(quantity)
