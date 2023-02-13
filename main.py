import sqlite3
import pandas as pd

CSV_FILENAME = "input_data/Sales.csv"
DB_NAME = "database_files/sample.db"
DB_TABLE = "sample"
TABLE_COLUMNS = []
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
reader = pd.read_csv(CSV_FILENAME)
df = pd.DataFrame(reader)


def df_to_sql():
    sql_db = df.to_sql(name=DB_TABLE, con=conn, if_exists="replace", index=False)
    for item in df.columns:
        TABLE_COLUMNS.append(item)
    return sql_db



df_to_sql()
print(TABLE_COLUMNS)