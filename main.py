import sqlite3
from store.store_inventory import StoreInventory
from store.store_clients import StoreClients
from store.store_orders import StoreOrders


class StoreApp:
    def __init__(self):
        pass

    @staticmethod
    def add_new_item(item_id, item_name, item_price, item_quantity):
        item.add_item_to_inventory(item_id, item_name, item_price, item_quantity)

    @staticmethod
    def show_items():
        item.show_store_inventory()

    @staticmethod
    def add_new_client(first_name, last_name, account_balance):
        clients.add_client(first_name, last_name, account_balance)
        pass


if __name__ == "__main__":
    item = StoreInventory()
    clients = StoreClients()
    app = StoreApp()
    app.add_new_item(1, "Computer", 100, 10)
    app.show_items()
