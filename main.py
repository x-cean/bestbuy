import products
from products import Product
import store
from store import Store


MENU = """   
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
Please choose a number: """


# set up initial stocks of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def start(a_store: Store):
    """
    return a string of menu
    """
    return MENU


def create_product_dict(a_store: Store):
    """
    create a product dictionary from a given Store Object
    """
    store_products = a_store.get_all_products()
    store_product_dict = {f"{i + 1}": store_products[i] for i in range(len(store_products))}
    return store_product_dict


def list_products(a_store: Store):
    """
    print all products with information
    """
    store_products = create_product_dict(a_store)
    print("------")
    for item_nr, item in store_products.items():
        print(item_nr + f". {store_products[item_nr].show()}")
    print("------")


def show_total_amount(a_store: Store):
    """
    show total amount of all items in store
    """
    print(f"Total items in store: {a_store.get_total_quantity()}")


def make_an_order(a_store: Store):
    """
    make an order
    buy the products (while stock quantity is enough)
    returns a total cost of the order
    """
    list_products(a_store)
    print("When you want to finish order, enter empty text.")
    product_dict = create_product_dict(a_store)
    shopping_list = []
    while True:
        user_input = input("Which product # do you want? ")
        user_input_2 = input("What amount do you want? ")
        if user_input == "":
            if shopping_list:
                try:
                    print(f"Order made! Total cost: {a_store.order(shopping_list)}")
                except Exception as e:
                    print(e)
            else:
                print("You didn't buy anything.")
            break
        elif user_input not in product_dict:
            print("Error adding product! ")
        else:
            try:
                shopping_list.append((product_dict[user_input], int(user_input_2)))
            except ValueError:
                print("Error adding product! ")


def quit_program(a_store: Store):
    """
    quit the program
    Store not used but this simplifies how I call the function in main, so I kept it here
    """
    print(f"Goodbye! We hope to see you again soon!")
    exit()


def main():
    """
    main function
    print menu
    executes user selected function
    """
    while True:
        user_input = input(start(best_buy))

        menu_dict = {
            "1": list_products,
            "2": show_total_amount,
            "3": make_an_order,
            "4": quit_program
        }

        try:
            menu_dict[user_input](best_buy)
        except KeyError:
            print()


if __name__ == "__main__":
    main()
