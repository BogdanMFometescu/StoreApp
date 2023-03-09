from store.store_clients import StoreClients
from store.store_inventory import StoreInventory
from store.store_orders import StoreOrders

item_in_store = StoreInventory()
clients = StoreClients()
orders = StoreOrders()


def create_db_table(table_name, primary_key, blank_column_name):
    table = f"CREATE TABLE IF NOT EXISTS {table_name} " \
            f"({primary_key} INTEGER PRIMARY KEY , {blank_column_name} TEXT "
    return table


def add_item_from_user_input():
    """Add new item in store from user input
    :param:item_id, item_name, item_price, item_quantity
    :return:values  of item_id, item_name, item_price, item_quantity"""
    print("Please enter new Item details (ID,Name,Price,Quantity)")
    try:
        item_id = int(input("Enter item ID:"))
        item_name = str(input("Enter item name:"))
        item_price = float(input("Enter item price :"))
        item_quantity = int(input("Enter item quantity :"))
        return item_id, item_name, item_price, item_quantity
    except ValueError:
        raise "Please enter valid info as required!"


def add_client_from_user_input():
    """Add new client to the store from user input
    :param:client_id, first_name,last_name,account_balance
    :return: values of client_id, first_name, last_name and account_balance"""
    print("Please enter new Client details (ID, First Name, Last Name, Account Balance)")
    try:
        client_id = int(input("Enter client ID:"))
        first_name = str(input("Enter client's first name :"))
        last_name = str(input("Enter client's last name:"))
        account_balance = int(input("Enter client's account balance:"))
        return client_id, first_name, last_name, account_balance
    except ValueError:
        raise "Please enter valid info as required!"


def add_and_check_order():
    """Add new order from user input
    :param:client_id, order_id, item_id, first_name, last_name, item_name, item_price,item_quantity
    :return: values of client_id, order_id, item_id, first_name, last_name, item_name, item_price,item_quantity
    """
    print("Please enter your order details:")
    try:
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

    except ValueError:
        raise "Please enter valid info required!"


