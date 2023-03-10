import pandas as pd

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

    def add_order(self, order_id: int, first_name: str, last_name: str, item_name: str, item_quantity: int,
                  item_price: float):
        """Add new order to the store and make a DataFrame with all the info
        :arg:order_id: int, first_name: str, last_name: str, item_name: str, item_quantity: int,
                  item_price: float
        :return:new order added, DataFrame with the store orders
        :raise:ValueError if order_id already exists
        """

        order = ClientOrder(order_id, first_name, last_name, item_name, item_quantity, item_price)
        self.order_list.append(order)
        if order_id not in self.order_id_list:

            self.order_id_list.append(order_id)
            self.order_first_name_list.append(first_name)
            self.order_last_name_list.append(last_name)
            self.order_item_name_list.append(item_name)
            self.order_quantity_list.append(item_quantity)
            self.order_item_price_list.append(item_price)

            df_order_id = pd.DataFrame(self.order_id_list, columns=[self.df_columns[0]])
            df_order_first_name = pd.DataFrame(self.order_first_name_list, columns=[self.df_columns[1]])
            df_order_last_name = pd.DataFrame(self.order_last_name_list, columns=[self.df_columns[2]])
            df_order_item_name = pd.DataFrame(self.order_item_name_list, columns=[self.df_columns[3]])
            df_order_quantity = pd.DataFrame(self.order_quantity_list, columns=[self.df_columns[4]])
            df_order_item_price = pd.DataFrame(self.order_item_price_list, columns=[self.df_columns[5]])

            df_orders_joined = df_order_id.join(
                [df_order_first_name, df_order_last_name, df_order_item_name, df_order_quantity, df_order_item_price])

            self.df_orders = df_orders_joined
            return self.df_orders
        else:
            raise f"{ValueError} Order ID already in use!"

    def get_all_orders(self):
        """Get all orders from the store in a DataFrame format
        :arg:self
        :return:all orders in DataFrame format"""
        return self.df_orders

    def show_orders(self):
        """Show all orders from the store
        :arg:self
        :return: print all store orders"""
        print(self.df_orders)
