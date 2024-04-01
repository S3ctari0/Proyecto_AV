class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class ProductViewerStrategy:
    def show_product_details(self, product):
        pass

class BasicProductViewer(ProductViewerStrategy):
    def show_product_details(self, product):
        print(f"Name: {product.name}")
        print(f"Description: {product.description}")
        print(f"Price: ${product.price}")

class CartManagerStrategy:
    def add_to_cart(self, product, quantity):
        pass

    def view_cart(self):
        pass

class BasicCartManager(CartManagerStrategy):
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product, quantity):
        self.cart.append((product, quantity))

    def view_cart(self):
        total_price = 0
        for product, quantity in self.cart:
            total_price += product.price * quantity
            print(f"{product.name} x{quantity}: ${product.price * quantity}")
        print(f"Total Price: ${total_price}")

class OrderProcessorStrategy:
    def process_order(self, cart, user_info, payment_info):
        pass

class BasicOrderProcessor(OrderProcessorStrategy):
    def process_order(self, cart, user_info, payment_info):
        print("Order processed successfully!")
        print("Items:")
        total_price = 0
        for product, quantity in cart:
            print(f"{product.name} x{quantity}")
            total_price += product.price * quantity
        print("Shipping to:")
        print(user_info)
        print("Total Price: ${}".format(total_price))
        print("Payment information:")
        print(payment_info)
        print("Thank you for your purchase!")
