class Order:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def add_item(self, product):
        self.items.append(product)

    def total(self):
        return sum(item.total_price() for item in self.items)
