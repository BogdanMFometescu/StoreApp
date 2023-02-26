import pandas as pd
from store.store_item import Item


class StoreInventory:
    """Perform operations to the store inventory: adding, removing and modify store items"""

    def __init__(self):
        self.df_inventory = None
        self.df_columns = ["ITEM_ID", "ITEM_NAME", "ITEM_PRICE", "ITEM_QUANTITY"]
        self.item_id_list = []
        self.item_name_list = []
        self.item_price_list = []
        self.item_quantity_list = []
        self.inventory_items = []

    def add_item_to_inventory(self, item_id, item_name, item_price, item_quantity):
        item = Item(item_id, item_name, item_price, item_quantity)
        self.inventory_items.append(item)

        # Append item to each specific list
        self.item_id_list.append(item_id)
        self.item_name_list.append(item_name)
        self.item_price_list.append(item_price)
        self.item_quantity_list.append(item_quantity)

        # Make df for each item
        df_id = pd.DataFrame(self.item_id_list, columns=[self.df_columns[0]])
        df_name = pd.DataFrame(self.item_name_list, columns=[self.df_columns[1]])
        df_price = pd.DataFrame(self.item_price_list, columns=[self.df_columns[2]])
        df_quantity = pd.DataFrame(self.item_quantity_list, columns=[self.df_columns[3]])

        df_item_joined = df_id.join([df_name, df_price, df_quantity])
        self.df_inventory = df_item_joined
        return self.df_inventory

    def remove_item_by_name(self, item_name):
        self.df_inventory = self.df_inventory[self.df_inventory.ITEM_NAME != item_name]

    def remove_item_by_id(self, item_id):
        self.df_inventory = self.df_inventory[self.df_inventory.ITEM_ID != item_id]

    def update_item_price(self, item_id, item_new_price):
        self.df_inventory.loc[self.df_inventory["ITEM_ID"] == item_id, "ITEM_PRICE"] = item_new_price

    def update_item_quantity(self, item_id, item_new_quantity):
        self.df_inventory.loc[self.df_inventory["ITEM_ID"] == item_id, "ITEM_QUANTITY"] = item_new_quantity

    def update_item_name(self, item_id, item_new_name):
        self.df_inventory.loc[self.df_inventory["ITEM_ID"] == item_id, "ITEM_NAME"] = item_new_name


st = StoreInventory()
st.add_item_to_inventory(1, "Keyboard", 100, 11)
st.add_item_to_inventory(2, "Computer", 200, 21)
st.add_item_to_inventory(3, "Monitor", 300, 32)

