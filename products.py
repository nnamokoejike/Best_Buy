from abc import ABC, abstractmethod


class Product:
    def __init__(self, name, price, quantity=0):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None

    def get_quantity(self):
        return self.quantity

    def is_active(self):
        return self.quantity > 0

    def show(self):
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}{promotion_info}"

    def set_promotion(self, promotion):
        self.promotion = promotion

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Insufficient quantity")
        self.quantity -= quantity
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def is_active(self):
        return True


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError("Exceeds maximum limit per order")
        return super().buy(quantity)


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        full_price_quantity = (quantity + 1) // 2
        half_price_quantity = quantity // 2
        return product.price * full_price_quantity + (product.price * half_price_quantity / 2)


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        full_price_quantity = quantity - (quantity // 3)
        return product.price * full_price_quantity
