from bestbuy.products import Product


class Store:
    def __init__(self, product_list):
        if not product_list:
            raise ValueError("Store must have at least one product.")
        for product in product_list:
            if type(product) != Product:
                raise TypeError("All products must be of type Product.")
        self.product_list = product_list

    def add_product(self, product):
        if type(product) != Product:
            raise TypeError("All products must be of type Product.")
        if product in self.product_list:
            raise ValueError("Product already exists in store.")
        self.product_list.append(product)

    def remove_product(self, product):
        if type(product) != Product:
            raise TypeError("All products must be of type Product.")
        if product not in self.product_list:
            raise ValueError("Product does not exist in store.")
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        if not self.product_list:
            return 0
        else:
            total_quantity = sum(product.quantity for product in self.product_list)
            return total_quantity

    def get_all_products(self) -> list:
        if not self.product_list:
            return []
        else:
            return [product for product in self.product_list if product.active]

    def order(self, shopping_list) -> float:
        pass