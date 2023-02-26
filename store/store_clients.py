import pandas as pd

from client.client import Client


class StoreClients:
    """Manage store clients, adding, removing, modify clients"""

    def __init__(self):
        self.df_clients = None
        self.df_columns = ["FIRST_NAME", "LAST_NAME", "ACCOUNT_BALANCE"]
        self.first_name_list = []
        self.last_name_list = []
        self.account_balance_list = []
        self.clients_list = []

    def add_client(self, first_name, last_name, account_balance):
        client = Client(first_name, last_name, account_balance)
        self.clients_list.append(client)

        self.first_name_list.append(first_name)
        self.last_name_list.append(last_name)
        self.account_balance_list.append(account_balance)

        df_first_name = pd.DataFrame(self.first_name_list, columns=[self.df_columns[0]])
        df_last_name = pd.DataFrame(self.last_name_list, columns=[self.df_columns[1]])
        df_account_balance = pd.DataFrame(self.account_balance_list, columns=[self.df_columns[2]])
        df_clients_joined = df_first_name.join([df_last_name, df_account_balance])
        self.df_clients = df_clients_joined
        return self.df_clients

    def remove_client_name(self, first_name, last_name):
        self.df_clients = self.df_clients[(self.df_clients.FIRST_NAME != first_name) &
                                          (self.df_clients.LAST_NAME != last_name)]




    def deposit_money(self, amount_deposited):
        pass


    def withdraw_money(self,amount_withdrawn):
        pass


    def update_balance(self):
        pass