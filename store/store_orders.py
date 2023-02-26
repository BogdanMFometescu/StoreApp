from client.client_order import ClientOrder


class StoreOrders:

    def __init__(self):
        self.df_orders = None
        self.df_columns = ["ORDER_ID", "FIRST_NAME", "LAST_NAME", "ITEM_NAME", "ITEM_QUANTITY", "ITEM_PRICE"]
        self.order_id_list = []
        self.order_first_name_list = []
        self.order_last_name_list = []
        self.order_item_name_list = []
        self.order_quantity_list = []
        self.order_item_price_list = []
        self.order_list = []

    def add_new_order(self, order_id, first_name, last_name, item_name, item_quantity, item_price):
        order = ClientOrder(order_id, first_name, last_name, item_name, item_quantity, item_price)
        self.order_list.append(order)

        self.order_id_list.append(order_id)
        self.order_first_name_list.append(first_name)
        self.order_last_name_list.append(last_name)
        self.order_item_name_list.append(item_name)
        self.order_quantity_list.append(item_quantity)
        self.order_item_price_list.append(item_price)

