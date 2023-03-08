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

    def add_item_to_inventory(self, item_id: int, item_name: str, item_price: float, item_quantity: int):
        """Add new item to the store inventory and check if item already exists, based on item_id.
        :arg:item_id: int, item_name: str, item_price: float, item_quantity: int
        :return: item added to inventory and DataFrame update if item not in list
        :raise: ValueError if item already in store, based on item_id """

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

    def remove_item_by_name(self, item_name: str):
        """Remove item from the store based on item_name
        :arg:item_name:str
        :return: item removed from the store and DataFrame updated
        """
        self.df_inventory = self.df_inventory[self.df_inventory.ITEM_NAME != item_name]

    def remove_item_by_id(self, item_id: int):
        """Remove item from the store based on item_id
        :arg:item_id:int
        :return:item removed from the store and DataFrame updated
        """
        self.df_inventory = self.df_inventory[self.df_inventory.ITEM_ID != item_id]

    def update_item_price(self, item_id: int, item_new_price: float):
        """Update item price based on item_id
        :arg:item_id:int, item_new_price:float
        :return: item_price and DataFrame updated"""
        self.df_inventory.loc[self.df_inventory["ITEM_ID"] == item_id, "ITEM_PRICE"] = item_new_price

    def update_item_quantity(self, item_id: int, item_new_quantity: int):
        """Update item quantity based on item_id
        :arg:item_id:int, item_new_quantity:int
        :return: item_quantity and DataFrame updated"""
        value = self.df_inventory.loc[self.df_inventory["ITEM_ID"] == item_id, "ITEM_QUANTITY"]
        updated_value = value - item_new_quantity
        self.df_inventory.loc[self.df_inventory["ITEM_ID"] == item_id, "ITEM_QUANTITY"] = updated_value

    def update_item_name(self, item_id: int, item_new_name: str):
        """Update item_name based on item_id
        :arg:item_id: int, item_new_name:str
        :return: item_name and DataFrame updated"""
        self.df_inventory.loc[self.df_inventory["ITEM_ID"] == item_id, "ITEM_NAME"] = item_new_name

    def check_inventory(self, item_name: str, item_price: float, item_quantity: int):
        """Check inventory when a client purchases an item
        :arg:item_name:str, item_price:float, item_quantity:int
        :return: True if item_name, item_price and item_quantity are correct
                 False if any of the args are not correct
        """
        count = 0
        val = self.df_inventory.loc[self.df_inventory["ITEM_NAME"] == item_name, "ITEM_QUANTITY"]

        if item_name in self.df_inventory["ITEM_NAME"].values:
            count += 1
        else:
            print(f"Item {item_name} not available !")

        if item_price in self.df_inventory["ITEM_PRICE"].values:
            count += 1
        else:
            print(f"Item price {item_price} is wrong!.Please check again")

        if item_quantity <= val.values:
            count += 1
        else:
            print(f"We have only  {val.values}  {item_name} in stock, order can't be processed!")

        if count == 3:
            print(f"Order under processing :Item: {item_name}, Price : {item_price} , Quantity : {item_quantity} !\n"
                  f"Total amount to pay : {item_price * item_quantity} $")
            return True
        else:
            print("Order is rejected, please try again!")
            return False

    def show_store_inventory(self):
        """Show the store inventory
        :arg:self
        :return: print items in store in DataFrame format"""
        print(self.df_inventory)

    def get_all_inventory_items(self):
        """Get all the items in store in DataFrame format
        :arg:self
        :return: all items in store in a DataFrame format"""
        return self.df_inventory
