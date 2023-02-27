import pandas as pd

from client.client import Client


class StoreClients:
    """Manage store clients: adding, removing and  modify clients info"""

    def __init__(self):
        self.df_clients = None
        self.df_columns = ["CLIENT_ID", "FIRST_NAME", "LAST_NAME", "ACCOUNT_BALANCE"]
        self.client_id_list = []
        self.first_name_list = []
        self.last_name_list = []
        self.account_balance_list = []
        self.clients_list = []

    def add_client(self, client_id, first_name, last_name, account_balance):
        client = Client(client_id, first_name, last_name, account_balance)
        self.clients_list.append(client)
        if client_id not in self.client_id_list:

            # Append item to each specific list
            self.client_id_list.append(client_id)
            self.first_name_list.append(first_name)
            self.last_name_list.append(last_name)
            self.account_balance_list.append(account_balance)

            # Make df for each item
            df_client_id = pd.DataFrame(self.client_id_list, columns=[self.df_columns[0]])
            df_first_name = pd.DataFrame(self.first_name_list, columns=[self.df_columns[1]])
            df_last_name = pd.DataFrame(self.last_name_list, columns=[self.df_columns[2]])
            df_account_balance = pd.DataFrame(self.account_balance_list, columns=[self.df_columns[3]])
            df_clients_joined = df_client_id.join([df_first_name, df_last_name, df_account_balance])
            self.df_clients = df_clients_joined

            return self.df_clients
        else:
            raise f"{ValueError} Client ID already in use!"

    def remove_client_name(self, first_name, last_name):
        self.df_clients = self.df_clients[(self.df_clients.FIRST_NAME != first_name) &
                                          (self.df_clients.LAST_NAME != last_name)]

    def update_balance(self, first_name, last_name, new_account_balance):
        self.df_clients.loc[(self.df_clients["FIRST_NAME"] == first_name) &
                            (self.df_clients["LAST_NAME"] == last_name), "ACCOUNT_BALANCE"] = new_account_balance

    def get_all_store_clients(self):
        return self.df_clients

    def show_store_clients(self):
        print(self.df_clients)

    def check_client_info(self, client_id, first_name, last_name):
        temp_list = [client_id, first_name, last_name]
        if all(value in self.df_clients.values for value in temp_list):
            print(f"Client with id : {client_id} , First Name : {first_name} and Last Name : {last_name} was found!")
            return True
        else:
            print(f"Client with id : {client_id} , First Name : {first_name} and Last Name : {last_name} was NOT found!")
            return False
