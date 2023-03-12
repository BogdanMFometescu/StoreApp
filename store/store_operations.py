import sqlite3

import pandas as pd

from helper_functions.helper_func import *
from store.store_clients import StoreClients
from store.store_inventory import StoreInventory
from store.store_orders import StoreOrders


class StoreOperations:
    """ Main class for the app, which allows users to perform different actions on a virtual store:
    add, remove, update store items
    add, remove clients
    submit and check clients orders
    send data to a sqlite database"""

    def __init__(self):
        self.DB_NAME = "STORE.sqlite"
        self.conn = sqlite3.connect(self.DB_NAME)
        self.cursor = self.conn.cursor()

    def create_db_table_for_items(self, primary_key: int = 1, blank_column_name: str = ""):
        table_name = ["ITEMS", "CLIENTS", "ORDERS"]
        """Create a table in sqlite database
        :arg: table_name, primary_key, blank_colum_name
        :return sqlite tables for items, clients and orders"""
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
    def add_new_item():
        """Add new item to the store
        :param:item_id, item_name,item_price,item_quantity
        :return: item added to the store,based on user input"""
        item = add_item_from_user_input()
        item_in_store.add_item_to_inventory(*item)

    @staticmethod
    def remove_item_by_name(item_name: str):
        """Remove an item from the store based on item name
        :arg:item_name
        :return: item removed from the store """
        item_in_store.remove_item_by_name(item_name)

    @staticmethod
    def remove_item_by_id(item_id: int):
        """Remove an item from the store based on item id
        :arg:item_id
        :return: item removed from the store """
        item_in_store.remove_item_by_id(item_id)

    @staticmethod
    def update_price(item_id: int, item_price: float):
        """Update the item price based on item_id and item_price
        :arg:item_id, item_price
        :return: item_price updated"""
        item_in_store.update_item_price(item_id, item_price)

    @staticmethod
    def update_quantity(item_id, item_new_quantity):
        """Update the item quantity in the store based on the item_id
        :arg:item_id, item_new_quantity
        :return:item quantity updated"""
        item_in_store.update_item_quantity(item_id, item_new_quantity)

    @staticmethod
    def add_new_client():
        """Add new client to the store based on attributes of Client class
        :arg:client_id, first_name, last_name, account_balance
        :return: new client added to the store"""
        client = add_client_from_user_input()
        clients.add_client(*client)

    @staticmethod
    def remove_store_client(first_name: str, last_name: str):
        """Remove a client from the store based on first name and last name
        :arg:first_name, last_name
        :return: client removed from the store"""
        clients.remove_client(first_name, last_name)

    @staticmethod
    def submit_and_check_order():
        """Check client order based on balance, availability of item and client info
        :arg:client_id, order_id, first_name, last_name, item_name, item_price, item_quantity
        :return: order confirmed or rejected"""
        print("Please enter your order details:")
        client_id = int(input("Enter Client ID:"))
        order_id = int(input("Enter Order ID:"))
        item_id = int(input("Enter Item ID:"))
        first_name = str(input("Enter client's first name :"))
        last_name = str(input("Enter client's last name:"))
        item_name = str(input("Enter item name:"))
        item_price = int(input("Enter item price :"))
        item_quantity = int(input("Enter item quantity :"))

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
        """Show store orders
        :arg:None
        :return: list of orders in store in DataFrame format"""
        orders.show_orders()

    @staticmethod
    def show_items():
        """Show store items from inventory
        :arg:None
        :return: list of items in the store in DataFrame format"""
        item_in_store.show_store_inventory()

    @staticmethod
    def show_clients():
        """Show store items from inventory
        :arg:None
        :return: list of clients  in the store in DataFrame format"""
        clients.show_store_clients()

    @staticmethod
    def run_app():
        while True:
            show_menu()
            menu_choice = input()
            match menu_choice:
                case "1":
                    app.add_new_item()
                case "2":
                    app.add_new_client()
                case "3":
                    app.submit_and_check_order()

                case "4":
                    app.show_items()

                case "5":
                    app.show_clients()

                case "6":
                    app.show_orders()

                case "7":
                    app.create_db_table_for_items()

                case "0":
                    break


item_in_store = StoreInventory()
clients = StoreClients()
orders = StoreOrders()
app = StoreOperations()
