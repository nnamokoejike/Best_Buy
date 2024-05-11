import products
from store import Store


def start(store_obj):
    while True:
        print("\nWelcome to JB Tech Equipment Store: ")
        print("1. List all products in store")
        print("2. Show total amount in store ")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            print("\nList of all products in store: ")
            for product in store_obj.get_all_products():
                print(product.show())

        elif choice == "2":
            print(f"Total of {store_obj.get_total_quantity()} Items in store")

        elif choice == "3":
            shopping_list = []
            while True:
                for product in store_obj.get_all_products():
                    print(product.show())

                product_name = input("\nEnter the name of the product (or 'done' to finish): ")
                if product_name.lower() == 'done':
                    break

                product = None
                for p in best_buy.get_all_products():
                    if p.name.lower() == product_name.lower():
                        product = p
                        break

                if product is None:
                    print(f"\nProduct '{product_name}' not found in the store.\n ")
                    continue

                quantity = int(input(f"Enter the quantity of {product.name} to order: "))
                if quantity <= 0:
                    print("Quantity should be greater than zero.")
                    continue

                if quantity > product.quantity:
                    print(f"Insufficient stock for {product.name}. Available quantity: {product.quantity}")
                    continue

                shopping_list.append((product, quantity))

                order_cost = store_obj.order(shopping_list)
                print(f"\nOrder placed! Total cost: ${order_cost}")

        elif choice == "4":
            print("Thank you very much today for using JB Tech Equipment Store. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = Store(product_list)
start(best_buy)