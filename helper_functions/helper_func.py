def create_db_table(table_name, primary_key, blank_column_name):
    table = f"CREATE TABLE IF NOT EXISTS {table_name} " \
            f"({primary_key} INTEGER PRIMARY KEY , {blank_column_name} TEXT "
    return table






