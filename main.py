import sqlite3
import pandas as pd

CSV_PATH = ""
DB_PATH = ""

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

