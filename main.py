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
    def add_new_client(client_id, first_name, last_name, account_balance):
        clients.add_client(client_id, first_name, last_name, account_balance)

    @staticmethod
    def show_clients():
        clients.show_store_clients()

    @staticmethod
    def add_new_order(client_id, order_id, first_name, last_name, item_name,  item_price,item_quantity):
        if clients.check_client_info(client_id, first_name, last_name) and item.check_inventory(item_name, item_price,
                                                                                                item_quantity):
            orders.add_order(order_id, first_name, last_name, item_name, item_quantity, item_price)
        else:
            print("Order is rejected, please try again!")

    @staticmethod
    def show_orders():
        orders.show_orders()


if __name__ == "__main__":
    item = StoreInventory()
    clients = StoreClients()
    orders = StoreOrders()
    app = StoreApp()

    app.add_new_item(1, "Computer", 10, 100)
    app.add_new_item(2, "Keyboard", 200, 10)
    app.add_new_item(3, "Keyboard", 200, 10)
    app.add_new_client(1, "John", "Doe", 1000)
    app.add_new_client(2, "Jane", "Dane", 2000)
    app.add_new_order(1, 1, "John", "Doe", "Computer", 10, 99)

