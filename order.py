class Order:
    """Класс для управления заказом и его товарами."""

    def __init__(self, items=None):
        """Создаёт заказ со списком товаров."""
        self.items = items if items is not None else []

    def add_item(self, product):
        """Добавляет товар в заказ."""
        self.items.append(product)

    def total(self):
        """Возвращает общую стоимость заказа."""
        return sum(item.total_price() for item in self.items)