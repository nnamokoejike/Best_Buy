class Store:
    def __init__(self, product_list):
        """
        Initialize a Store object.

        Args:
            product_list (list): A list of Product objects representing the initial inventory.
        """
        self.products = product_list

    def add_product(self, product):
        """
        Add a product to the store's inventory.

        Args:
            product (Product): The product to add to the inventory.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store's inventory.

        Args:
            product (Product): The product to remove from the inventory.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """
        Get the total quantity of all active products in the store.

        Returns:
            int: The total quantity of all active products.
        """
        total_quantity = sum(product.get_quantity() for product in self.products)
        return total_quantity

    def get_all_products(self):
        """
        Get all active products in the store.

        Returns:
            list: A list of all active products.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """
        Place an order for products in the store.

        Args:
            shopping_list (list): A list of tuples where each tuple contains a Product object and the quantity to order.

        Returns:
            float: The total cost of the order.

        Raises:
            ValueError: If a product in the shopping list is not available in the store.
        """
        total_price = 0

        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"{product.name} is not available in the store.")
            total_price += product.buy(quantity)

        return total_price
