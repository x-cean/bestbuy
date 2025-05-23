"""
In the style check I was asked to use isinstance(), is this the most standard
method compare to

if type(quanlity) != int

please? Cheers!

if not isinstance(quantity, int)
"""


import products
from products import Product


class Store:
    """Store Object, comes with a list of Products"""
    def __init__(self, product_list):
        """
        Initiator (constructor) method.
        Each Store will have a list of Products
        """
        if not product_list:
            raise ValueError("Store must have at least one product.")
        for product in product_list:
            if not isinstance(product, Product):
                raise TypeError("All products must be of type Product.")
        self.product_list = product_list

    def add_product(self, product):
        """
        Adds new Product
        """
        if not isinstance(product, Product):
            raise TypeError("All products must be of type Product.")
        if product in self.product_list:
            raise ValueError("Product already exists in store.")
        self.product_list.append(product)

    def remove_product(self, product):
        """
        Removes a Product from Store.
        """
        if not isinstance(product, Product):
            raise TypeError("All products must be of type Product.")
        if product not in self.product_list:
            raise ValueError("Product does not exist in store.")
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns how many items are in the store in total.
        """
        if not self.product_list:
            return 0
        total_quantity = sum(product.quantity for product in self.product_list)
        return total_quantity

    def get_all_products(self) -> list:
        """
        Returns all products in the store that are active.
        """
        if not self.product_list:
            return []
        return [product for product in self.product_list if product.active]

    def order(self, shopping_list) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        if not isinstance(shopping_list, list):
            raise TypeError("Shopping list must be a list of tuple with Product "
                            "objects and quantities.")
        if not shopping_list:
            raise ValueError("Shopping list cannot be empty.")
        total_cost = 0
        for product, quantity in shopping_list:
            if not isinstance(product, Product):
                raise TypeError("All products must be of type Product.")
            if not isinstance(quantity, int):
                raise TypeError("All quantities must be integers.")
            if product not in self.product_list or product.quantity < quantity:
                if total_cost > 0:
                    print("Order made! Total cost: ", total_cost, " dollars.")
                raise ValueError("Error while making order! Quantity larger than what exists.")
            else:
                total_cost += product.buy(quantity)
        return total_cost

def test_store():
    """
    test from codio assignment 1
    """
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)

    best_buy = Store([bose, mac])
    price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
    print(f"Order cost: {price} dollars.")

def main():
    """
    tests from codio assignment
    """
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    best_buy_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(best_buy_products[0], 1), (best_buy_products[1], 2)]))
    print("New total: ", best_buy.get_total_quantity())
    test_store()
    print("New total: ", best_buy.get_total_quantity())


if __name__ == "__main__":
    main()
