from abc import ABC, abstractmethod  # Importing ABC and abstractmethod for creating abstract classes


class Promotion(ABC):
    def __init__(self, name):
        """
        Initialize a Promotion object.

        Args:
            name (str): The name of the promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Apply the promotion to a product.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the promotion.
        """
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        """
        Initialize a PercentDiscount object.

        Args:
            name (str): The name of the promotion.
            percent (float): The percentage discount.
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """
        Apply the percentage discount promotion to a product.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the promotion.
        """
        discount = (self.percent / 100) * product.price
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        """
        Initialize a SecondHalfPrice object.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Apply the second half price promotion to a product.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the promotion.
        """
        if quantity < 2:
            return product.price * quantity
        else:
            full_price_qty = quantity // 2
            half_price_qty = quantity - full_price_qty
            return (full_price_qty * product.price) + (half_price_qty * product.price * 0.5)


class ThirdOneFree(Promotion):
    def __init__(self, name):
        """
        Initialize a ThirdOneFree object.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        Apply the third one free promotion to a product.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the promotion.
        """
        if quantity < 3:
            return product.price * quantity
        else:
            sets_of_three = quantity // 3
            remaining_items = quantity % 3
            return (sets_of_three * 2 * product.price) + (remaining_items * product.price)
