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
    print(MENU)


def create_product_dict(a_store: Store):
    store_products = a_store.get_all_products()
    store_product_dict = {f"{i + 1}": store_products[i] for i in range(len(store_products))}
    return store_product_dict


def list_products(a_store: Store):
    store_products = create_product_dict(a_store)
    print("------")
    for item_nr, item in store_products.items():
        print(item_nr + f". {store_products[item_nr].show()}")
    print("------")


def show_total_amount(a_store: Store):
    print(f"Total items in store: {a_store.get_total_quantity()}")


def make_an_order(a_store: Store):
    list_products(a_store)
    print("When you want to finish order, enter empty text.")
    item_nr, item = create_product_dict(a_store).items()
    shopping_list = []
    while True:
        user_input = input("Which product # do you want? ")
        if user_input == "":
            user_input_2 = input("What amount do you want? ")
            if user_input_2 == "":
                if shopping_list:
                    print(f"Total cost: {a_store.order(shopping_list)}")
                else:
                    print("You didn't buy anything.")
                break
        try:
            product_nr = int(user_input)
            if product_nr in store_products:
                quantity = int(input("Enter quantity: "))
                shopping_list.append((store_products[product_nr], quantity))


MENU_DICT = {"1": list_products,
#     "2": show_total_amount,
#     "3": make_an_order,
#     "4": quit_program
             }
