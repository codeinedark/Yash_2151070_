class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity, price):
        if item_name not in self.items:
            self.items[item_name] = {'quantity': quantity, 'price': price}
        else:
            self.items[item_name]['quantity'] += quantity

    def update_item(self, item_name, quantity=None, price=None):
        if item_name in self.items:
            if quantity:
                self.items[item_name]['quantity'] = quantity
            if price:
                self.items[item_name]['price'] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print("Item not found in inventory.")

    def generate_report(self):
        print("{:<10} {:<10} {:<10}".format('Item', 'Quantity', 'Price'))
        for item, details in self.items.items():
            print("{:<10} {:<10} {:<10}".format(item, details['quantity'], details['price']))


inventory = Inventory()


inventory.add_item('Apple', 10, 1.5)
inventory.add_item('Banana', 20, 0.5)

inventory.update_item('Apple', quantity=5)
inventory.update_item('Banana', price=0.75)


inventory.remove_item('Apple')


inventory.generate_report()
