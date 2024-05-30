import products  # Importing product classes
from store import Store  # Importing Store class
import promotions


def start(store_obj):
    """
    Start function to interact with the JB Tech Equipment Store.

    Args:
        store_obj (Store): The store object to interact with.
    """
    while True:
        # Displaying the main menu
        print("\nWelcome to JB Tech Equipment Store: ")
        print("1. List all products in store")
        print("2. Show total amount in store ")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")  # Getting user input for choice

        if choice == "1":  # Option to list all products in the store
            print("\nList of all products in store: ")
            for product in store_obj.get_all_products():
                print(product.show())  # Displaying each product details

        elif choice == "2":  # Option to show total amount of items in the store
            print(f"Total of {store_obj.get_total_quantity()} Items in store")

        elif choice == "3":  # Option to make an order
            shopping_list = []
            while True:
                for product in store_obj.get_all_products():
                    print(product.show())  # Displaying each product details

                product_name = input("\nEnter the name of the product (or 'done' to finish): ")
                if product_name.lower() == 'done':
                    break

                product = None
                for p in store_obj.get_all_products():
                    if p.name.lower() == product_name.lower():
                        product = p
                        break

                if product is None:
                    print(f"\nProduct '{product_name}' not found in the store.\n ")
                    continue
        elif choice == "4":
            print("Thank you very much today for using JB Tech Equipment Store. Goodbye!")
            break


# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)

best_buy = Store(product_list)

start(best_buy)
