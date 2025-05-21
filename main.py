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
start(best_buy)