class ShoppingCart:
    def _init_(self):
        self.cart = { }

    def add_item(self, item_name, price, quantity=1):
        self.cart[item_name] = self.cart.get(item_name, {'price': price, 'quantity': 0})
        self.cart[item_name]['quantity'] += quantity

    def remove_item(self, item_name, quantity=1):
        if item_name in self.cart:
            
            self.cart[item_name]['quantity'] -= quantity
            if self.cart[item_name]['quantity'] <= 0:
                 del self.cart[item_name]

    def print_bill(self):
        total = 0
        print("Bill:")
        for item_name, details in self.cart.items():
            item_total = details['price'] * details['quantity']
            print(f"{item_name}: ${details['price']} x {details['quantity']} = ${item_total}")
            total += item_total
        print(f"Total: ${total}")


cart = ShoppingCart()
cart.add_item("Apple", 0.5, 3)
cart.add_item("Banana", 0.3, 2)
cart.remove_item("Apple", 1)
cart.print_bill()
