def create_db_table(table_name, primary_key, blank_column_name ):
    table = f"CREATE TABLE IF NOT EXISTS {table_name} " \
            f"({primary_key} INTEGER PRIMARY KEY , {blank_column_name} TEXT "
    return table





def add_items_to_db(table_name, item_id, item_name, item_price, item_quantity):
    values = f"INSERT INTO {table_name} ({item_id}, {item_name}, {item_price},{item_quantity}) VALUES (?,?,?,?)"
    return values


def select_all_columns(table_name):
    select_all = f"SELECT * FROM {table_name} "
    return select_all


def search_by_row(table_name, row_name):
    select_colum = f"SELECT * FROM {table_name} WHERE {row_name} =?"
    return select_colum


def delete_row(table_name, row_name):
    select_row = f"DELETE FROM {table_name} WHERE {row_name} = ?"
    return select_row


def update_value(table_name, col_name):
    name = f"UPDATE {table_name} SET {col_name} = ? WHERE {col_name}= ?"
    return name

