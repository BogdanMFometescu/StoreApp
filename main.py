from store.store_inventory import StoreInventory
from store.store_clients import StoreClients
from store.store_orders import StoreOrders
from helper_functions.helper_func import create_db_table
import sqlite3
import pandas as pd


class StoreApp:
    """ Main class for the app, which allows users to perform different actions on a virtual store:
    add, remove, update store items
    add, remove clients
    submit and check clients orders
    send data to a sqlite database"""
    def __init__(self):
        self.DB_NAME = "STORE.sqlite"
        self.conn = sqlite3.connect(self.DB_NAME)
        self.cursor = self.conn.cursor()

    def create_db_table_for_items(self, table_name: list, primary_key: int = 1, blank_column_name: str = ""):
        # Create tables in db for items, clients and orders
        create_db_table(table_name, primary_key, blank_column_name)

        # Get DataFrame for items, clients and orders
        df_items = item_in_store.get_all_inventory_items()
        df_clients = clients.get_all_store_clients()
        df_orders = orders.get_all_orders()

        # Create new DataFrame for items, clients and orders
        items_df = pd.DataFrame(df_items)
        clients_df = pd.DataFrame(df_clients)
        orders_df = pd.DataFrame(df_orders)

        # Populate database with items from DataFrame
        sql_table_items = items_df.to_sql(name=table_name[0], con=self.conn, if_exists="replace", index=False)
        sql_table_clients = clients_df.to_sql(name=table_name[1], con=self.conn, if_exists="replace", index=False)
        sql_table_orders = orders_df.to_sql(name=table_name[2], con=self.conn, if_exists="replace", index=False)

        return sql_table_items, sql_table_clients, sql_table_orders

    @staticmethod
    def add_new_item(item_id: int, item_name: str, item_price: float, item_quantity: int):
        item_in_store.add_item_to_inventory(item_id, item_name, item_price, item_quantity)

    @staticmethod
    def remove_item_by_name(item_name: str):
        item_in_store.remove_item_by_name(item_name)

    @staticmethod
    def remove_item_by_id(item_id: int):
        item_in_store.remove_item_by_id(item_id)

    @staticmethod
    def update_price(item_id: int, item_price: float):
        item_in_store.update_item_price(item_id, item_price)

    @staticmethod
    def update_quantity(item_id, item_quantity):
        item_in_store.update_item_quantity(item_id, item_quantity)

    @staticmethod
    def add_new_client(client_id: int, first_name: str, last_name: str, account_balance: int):
        clients.add_client(client_id, first_name, last_name, account_balance)

    @staticmethod
    def remove_store_client(first_name: str, last_name: str):
        clients.remove_client(first_name, last_name)

    @staticmethod
    def submit_and_check_order(client_id, order_id, item_id, first_name, last_name, item_name, item_price,
                               item_quantity):
        # Total amount to pay - invoice value
        invoice_value = item_price * item_quantity

        # Check if client, item and account balance are correct
        clients.check_client_info(client_id, first_name, last_name)
        item_in_store.check_inventory(item_name, item_price, item_quantity)
        clients.check_balance(client_id, invoice_value)

        # Confirm the order and update de store and client info
        orders.add_order(order_id, first_name, last_name, item_name, item_quantity, item_price)
        item_in_store.update_item_quantity(item_id, item_quantity)

    @staticmethod
    def show_orders():
        orders.show_orders()

    @staticmethod
    def show_items():
        item_in_store.show_store_inventory()

    @staticmethod
    def show_clients():
        clients.show_store_clients()


if __name__ == "__main__":
    item_in_store = StoreInventory()
    clients = StoreClients()
    orders = StoreOrders()
    app = StoreApp()

    # Add items to the store
    app.add_new_item(1, "Computer", 10, 100)
    app.add_new_item(2, "Keyboard", 200, 10)
    app.add_new_item(3, "Keyboard", 200, 10)

    # Add clients to the store
    app.add_new_client(1, "John", "Doe", 10000)
    app.add_new_client(2, "Jane", "Dane", 2000)
    app.add_new_client(3, "Bob", "Hope", 3000)

    # Submit and check order
    app.submit_and_check_order(1, 1, 1, "John", "Doe", "Computer", 10, 50)

    # Update sqlite database
    app.create_db_table_for_items(["ITEMS", "CLIENTS", "ORDERS"])
    print("*" * 70)
    # Show items, clients and orders
    app.show_items()
    print("*"*70)
    app.show_clients()
    print("*"*70)
    app.show_orders()
