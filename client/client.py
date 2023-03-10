class Client:

    def __init__(self, client_id: int, first_name: str, last_name: str, account_balance: int):
        assert client_id > 0, f"{ValueError} Client ID must be greater than zero "
        assert first_name.isspace() is False and first_name != "", f"{ValueError}Client first_name must be a String "
        assert last_name.isspace() is False and last_name != "", f"{ValueError}Client last_name must be a String "
        assert account_balance >= 0, f"{ValueError} Account balance must be greater or equal to zero"

        self._client_id = client_id
        self._first_name = first_name
        self._last_name = last_name
        self._account_balance = account_balance

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
    def account_balance(self):
        return self._account_balance

    @account_balance.setter
    def account_balance(self, value):
        self._account_balance = value

    def __repr__(self):
        return f"{self._client_id}, {self._first_name} , {self._last_name}, {self._account_balance}"

    def __str__(self):
        return f"{self._client_id}, {self._first_name} , {self._last_name}, {self._account_balance}"
