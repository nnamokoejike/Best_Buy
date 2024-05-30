from abc import ABC, abstractmethod  # Importing ABC and abstractmethod for creating abstract classes


class Product:
    def __init__(self, name, price, quantity=0):
        """
        Initialize a Product object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int, optional): The quantity of the product. Defaults to 0.

        Raises:
            ValueError: If any of the parameters are invalid.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None

    def get_quantity(self):
        """Get the quantity of the product."""
        return self.quantity

    def is_active(self):
        """Check if the product is active (i.e., quantity > 0)."""
        return self.quantity > 0

    def show(self):
        """
        Display information about the product.

        Returns:
            str: A string containing the product information.
        """
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}{promotion_info}"

    def set_promotion(self, promotion):
        """
        Set the promotion for the product.

        Args:
            promotion (Promotion): The promotion to set for the product.
        """
        self.promotion = promotion

    def buy(self, quantity):
        """
        Buy a certain quantity of the product.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity to buy exceeds the available quantity.
        """
        if quantity > self.quantity:
            raise ValueError("Insufficient quantity")
        self.quantity -= quantity
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity


class NonStockedProduct(Product):
    def __init__(self, name, price):
        """
        Initialize a NonStockedProduct object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
        """
        super().__init__(name, price, quantity=0)

    def is_active(self):
        """Check if the non-stocked product is always active."""
        return True


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        """
        Initialize a LimitedProduct object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The initial quantity of the product.
            maximum (int): The maximum quantity allowed per order.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """
        Buy a certain quantity of the limited product.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity to buy exceeds the maximum limit per order.
        """
        if quantity > self.maximum:
            raise ValueError("Exceeds maximum limit per order")
        return super().buy(quantity)


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
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        """
        Apply the second half price promotion to a product.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the promotion.
        """
        full_price_quantity = (quantity + 1) // 2
        half_price_quantity = quantity // 2
        return product.price * full_price_quantity + (product.price * half_price_quantity / 2)


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        """
        Apply the third one free promotion to a product.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the promotion.
        """
        full_price_quantity = quantity - (quantity // 3)
        return product.price * full_price_quantity
