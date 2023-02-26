class Client:

    def __init__(self, client_id, first_name: str, last_name: str, balance: float):
        self._client_id = client_id
        self._first_name = first_name
        self._last_name = last_name
        self._balance = balance

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def __repr__(self):
        pass
