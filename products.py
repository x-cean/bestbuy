class Product:
    def __init__(self, name, price, quantity):
        """
        Initiator (constructor) method.
        Creates the instance variables (active is set to True).
        If something is invalid (empty name / negative price or quantity), raises an exception.
        """
        self.active = True
        if not name:
            raise ValueError("Product name cannot be an empty string.")
        elif price < 0:
            raise ValueError("Product price cannot be negative.")
        elif type(price) != float and type(price) != int:
            raise ValueError("Product price must be a number.")
        elif quantity < 0:
            raise ValueError("Product quantity cannot be negative.")
        elif type(quantity) != int:
            raise ValueError("Product quantity must be an integer.")
        else:
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
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")
        elif quantity == 0:
            self.deactivate()
        else:
            self.quantity = quantity

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
        print(info)
        return info
        # the instruction wants a return, the demo main() wants a print, so I put both here

    def buy(self, quantity) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem, raises an Exception.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        elif type(quantity) != int:
            raise ValueError("Quantity must be an integer.")
        elif quantity > self.quantity:
            raise ValueError("Not enough quantity in stock.")
        else:
            self.quantity -= quantity
            if self.quantity == 0:
                self.deactivate()
            return self.price * quantity


def main():
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