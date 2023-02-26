class ClientOrder:
    def __init__(self, order_id: int, first_name, last_name, item_name, item_quantity, item_price):
        assert order_id > 0, f"{ValueError} Order id must be greater than zero"
        assert first_name.isspace() is False and first_name != "", f"{ValueError}Client first_name must be a String "
        assert last_name.isspace() is False and last_name != "", f"{ValueError}Client last_name must be a String "
        assert item_quantity > 0, f"{ValueError} Item quantity must be greater than zero"
        assert item_price > 0, f"{ValueError} Item price must be greater than zero"

        self._order_id = order_id
        self._first_name = first_name
        self._last_name = last_name
        self._item_name = item_name
        self._item_quantity = item_quantity
        self._item_price = item_price

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value

    @property
    def item_quantity(self):
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, value):
        self._item_quantity = value

    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, value):
        self._item_price = value

    def __repr__(self):
        return f"{self._order_id}, " \
               f"{self.first_name}," \
               f" {self._last_name}," \
               f"{self._item_quantity}," \
               f" {self._item_price}," \
               f"{self._item_name}"
