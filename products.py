class Product:
    """
    Product Object, comes with name, price and quantity.
    """
    def __init__(self, name, price, quantity):
        """
        Initiator (constructor) method.
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity), raises an exception.
        """
        self.active = True
        if not name:
            raise ValueError("Product name cannot be an empty string.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        if not isinstance(price, float) and not isinstance(price, int):
            raise ValueError("Product price must be a number.")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")
        if not isinstance(quantity, int):
            raise ValueError("Product quantity must be an integer.")
        self.name = name
        self.price = price
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def get_quantity(self) -> int:
        """
        Getter function for quantity.
        Returns the quantity (int).
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Setter function for quantity.
        If the quantity reaches 0, deactivates the product.
        """
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()
        elif quantity < 0:
            raise ValueError("Product quantity cannot be negative.")


    def is_active(self) -> bool:
        """
        Getter function for active.
        Returns True if the product is active, otherwise False.
        """
        return self.active

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self) -> str:
        """
        Returns a string that represents the product
        """
        info = f"{self.name}, Price: {self.price:.2f}, Quantity: {self.quantity}"
        # print(info)
        return info
        # the instruction wants a return, the given demo main() here wants a print
        # But I only need return for main.py

    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem, raises an Exception.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity in stock.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity


def main():
    """
    instructed tests from codio assignment
    """
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()
