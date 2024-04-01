from functions import Product, BasicProductViewer, BasicCartManager, BasicOrderProcessor

class OnlineStore:
    def __init__(self, product_viewer_strategy, cart_manager_strategy, order_processor_strategy):
        self.product_viewer = product_viewer_strategy()
        self.cart_manager = cart_manager_strategy()
        self.order_processor = order_processor_strategy()

    def browse_products(self, products):
        print("Available products:")
        for index, product in enumerate(products):
            print(f"{index + 1}. {product.name} - ${product.price}")

    def view_product_details(self, product):
        self.product_viewer.show_product_details(product)

    def select_products(self, products):
        while True:
            selection = input("Enter the product number to add to cart (or 'details' to view details, 'done' to finish): ")
            if selection.lower() == 'done':
                break
            elif selection.lower() == 'details':
                product_index = int(input("Enter the product number to view details: ")) - 1
                if 0 <= product_index < len(products):
                    self.view_product_details(products[product_index])
                else:
                    print("Invalid product number.")
            else:
                try:
                    index = int(selection) - 1
                    if 0 <= index < len(products):
                        quantity = int(input("Enter the quantity: "))
                        if quantity > 0:
                            self.cart_manager.add_to_cart(products[index], quantity)
                        else:
                            print("Quantity must be greater than 0.")
                    else:
                        print("Invalid product number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    def view_cart(self):
        self.cart_manager.view_cart()

    def process_order(self):
        if not self.cart_manager.cart:
            print("Your cart is empty. Please add some items before placing an order.")
            return
        
        user_info = input("Enter shipping information (e.g., address, city, country): ")
        payment_info = input("Enter payment information (e.g., credit card number): ")

        self.order_processor.process_order(self.cart_manager.cart, user_info, payment_info)

def main():
    # Initialize strategies
    product_viewer_strategy = BasicProductViewer
    cart_manager_strategy = BasicCartManager
    order_processor_strategy = BasicOrderProcessor

    # Create products
    products = [
        Product("Laptop", "High-performance laptop", 1000),
        Product("Smartphone", "Latest smartphone model", 800),
        Product("Headphones", "Noise-cancelling headphones", 200),
        Product("Tablet", "Lightweight tablet with touch screen", 400),
        Product("Camera", "Professional DSLR camera", 1500),
        Product("Smartwatch", "Fitness tracker and smartwatch", 300)
    ]

    # Create store instance
    online_store = OnlineStore(product_viewer_strategy, cart_manager_strategy, order_processor_strategy)

    # Browse products
    online_store.browse_products(products)

    # Select products to add to cart
    online_store.select_products(products)

    # View cart
    online_store.view_cart()

    # Process order
    online_store.process_order()

if __name__ == "__main__":
    main()