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


def show_menu():
    menu = ["Please choose an option from the menu:",
            "1. Add new item in store",
            "2. Add new client to the store",
            "3. Add and process new order",
            "4. List items in store",
            "5. List store clients",
            "6. List store orders",
            "7. Save data to database",
            "0. Quit"]

    for _, items in enumerate(menu):
        print(items)
