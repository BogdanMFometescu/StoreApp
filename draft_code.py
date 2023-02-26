import sqlite3
import pandas as pd
from helper_functions.helper_func import create_db_table

DB_NAME: str = input("Enter DB name:")
DB_TABLE_NAME: str = input("Enter DB TABLE NAME :")
DB_TEST_PRIMARY_KEY = 1
DB_TEST_COL_NAME = "Test"
CSV_FILENAME: str = "database_files/sample.db"
TABLE_COLUMNS: list = []

# 1 Create empty sqlite3 database with  default values

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# 2 Create an empty table in the db
create_db_table(DB_TABLE_NAME, DB_TEST_PRIMARY_KEY, DB_TEST_COL_NAME)

# 3 Get the *csv filename and make DataFrame
reader = pd.read_csv(CSV_FILENAME)
df = pd.DataFrame(reader)

# 4 Create table with data in sqlite db based on csv file
sql_table = df.to_sql(name=DB_TABLE_NAME, con=conn, if_exists="replace", index=False)

# 5 Add/Modify values in sqlite or df
for col in df.columns:
    print(col)

