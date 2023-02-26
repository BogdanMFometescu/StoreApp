class Item:
    def __init__(self, item_id: int, item_name: str, item_price: float, item_quantity: int):
        self._item_id = item_id
        self._item_name = item_name
        self._item_price = item_price
        self._item_quantity = item_quantity

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value

    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value

    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        self._item_price = value

    @property
    def item_quantity(self):
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, value):
        self._item_quantity = value

    def __repr__(self):
        return f"{self._item_id}, {self._item_name}, {self._item_price}, {self._item_quantity}"
