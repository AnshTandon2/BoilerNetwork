import sqlite3
import pandas as pd

csvPATH = "streamlitEmbed/data/data.csv"
dbPATH = "streamlitEmbed/data/opportunityDatabase.db"
dbName = "opportunityDatabase"

df = pd.read_csv(csvPATH)

df.columns = df.columns.str.strip()

conn = sqlite3.connect(dbPATH)

df.to_sql(dbName, conn, if_exists="replace")

# Commit changes and close the connection
conn.commit()
conn.close()
