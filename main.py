from store.store_inventory import StoreInventory
from store.store_clients import StoreClients
from store.store_orders import StoreOrders


class StoreApp:
    def __init__(self):
        pass

    @staticmethod
    def add_new_item(item_id: int, item_name: str, item_price: float, item_quantity: int):
        item_in_store.add_item_to_inventory(item_id, item_name, item_price, item_quantity)

    @staticmethod
    def add_new_client(client_id: int, first_name: str, last_name: str, account_balance: float):
        clients.add_client(client_id, first_name, last_name, account_balance)

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

    app.add_new_item(1, "Computer", 10, 100)
    app.add_new_item(2, "Keyboard", 200, 10)
    app.add_new_item(3, "Keyboard", 200, 10)
    app.add_new_client(1, "John", "Doe", 10000)
    app.add_new_client(2, "Jane", "Dane", 2000)
    app.submit_and_check_order(1, 1, 1, "John", "Doe", "Computer", 10, 100)
