class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if name in self.items:
            self.items[name].append(price)
        else:
            self.items[name] = [price]

    def remove_item(self, name):
        if name in self.items:
            self.items[name].pop()
            if not self.items[name]:
                del self.items[name]

    def total_cost(self):
        return sum(price for prices in self.items.values() for price in prices)


