from abc import ABC, abstractmethod


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
        discount = (self.percent / 100) * product.price
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity < 2:
            return product.price * quantity
        else:
            full_price_qty = quantity // 2
            half_price_qty = quantity - full_price_qty
            return (full_price_qty * product.price) + (half_price_qty * product.price * 0.5)


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity < 3:
            return product.price * quantity
        else:
            sets_of_three = quantity // 3
            remaining_items = quantity % 3
            return (sets_of_three * 2 * product.price) + (remaining_items * product.price)
