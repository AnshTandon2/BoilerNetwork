import sqlite3
import pandas as pd

# Connect to the database (or create it if it doesn't exist)
df = pd.read_csv("data.csv")

df.columns = df.columns.str.strip()

conn = sqlite3.connect('opportunityDatabase.db')

df.to_sql("opportunityDatabase.db", conn, if_exists="replace")

# Commit changes and close the connection
conn.commit()
conn.close()
