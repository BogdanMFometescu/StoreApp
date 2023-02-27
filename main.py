from store.store_inventory import StoreInventory
from store.store_clients import StoreClients
from store.store_orders import StoreOrders


class StoreApp:
    def __init__(self):
        pass

    @staticmethod
    def add_new_item(item_id, item_name, item_price, item_quantity):
        item.add_item_to_inventory(item_id, item_name, item_price, item_quantity)
        print(item.inventory_items)

    @staticmethod
    def show_items():
        item.show_store_inventory()

    @staticmethod
    def add_new_client(first_name, last_name, account_balance):
        clients.add_client(first_name, last_name, account_balance)

    @staticmethod
    def show_clients():
        clients.show_store_clients()

    @staticmethod
    def add_new_order(first_name, last_name, item_name, item_quantity, item_price):
        orders.add_order(1, first_name, last_name, item_name, item_quantity, item_price)

    @staticmethod
    def show_orders():
        orders.show_orders()


if __name__ == "__main__":
    item = StoreInventory()
    clients = StoreClients()
    orders = StoreOrders()
    app = StoreApp()
    app.add_new_item(1, "Computer", 100, 10)
    app.add_new_item(2, "Keyboard", 200, 10)
    app.add_new_client("John", "Doe", 1000)
    app.add_new_client("Jane", "Dane", 2000)

    app.show_items()
    app.show_clients()
