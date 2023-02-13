import sqlite3
import pandas as pd

CSV_FILENAME = "input_data/Sales.csv"
DB_NAME = "database_files/sample.db"
DB_TABLE = "sample"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


def read_csv_and_make_df(filename):
    reader = pd.read_csv(filename)
    df = pd.DataFrame(reader)
    return df


def send_to_sql_db():
    df = read_csv_and_make_df(filename=CSV_FILENAME)
    sql_db = df.to_sql(name=DB_TABLE, con=conn, if_exists="replace", index=False)
    return sql_db


send_to_sql_db()
