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
        # Append item to each specific list
        item = Item(item_id, item_name, item_price, item_quantity)
        self.inventory_items.append(item)

        if item_id not in self.item_id_list:
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
        else:
            raise f"{ValueError} ITEM ID already in use!"

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

    def show_store_inventory(self):
        print(self.df_inventory)

    def get_all_inventory_items(self):
        return self.df_inventory

    def check_inventory(self, item_name, item_price, item_quantity):
        val = self.df_inventory.loc[self.df_inventory["ITEM_NAME"] == item_name, "ITEM_QUANTITY"]

        if item_name in self.df_inventory["ITEM_NAME"].values:
            print(f"Item {item_name} was found in store!")
        else:
            print(f"Item {item_name} not available !")

        if item_price in self.df_inventory["ITEM_PRICE"].values:
            print(f"Item price {item_price} is correct !")
        else:
            print(f"Item price {item_price} is wrong!.Please check again")

        if item_quantity > val.values:
            print(f"We do not have {item_quantity} pieces of {item_name} in stock!")
            print(f"We have {val.values} in stock  for {item_name}")
        else:
            print(f"We have {val.values}  {item_name} in stock, order can be processed!")


st = StoreInventory()
st.add_item_to_inventory(1, "Computer", 10, 100)

st.check_inventory("Computer", 100, 10000)

