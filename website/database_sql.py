import sqlite3
import pandas as pd

# Step 1: Connect to your SQLite database
db_path = "/Users/himanshugusain/Desktop/django user project/website/db.sqlite3"
conn = sqlite3.connect(db_path)

# Step 2: Check what tables are available
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Available tables:\n", tables)

# Step 3: Choose a table to read (example: 'auth_user')
query = "SELECT * FROM main_post;"  # replace with your table name
df = pd.read_sql_query(query, conn)

# Step 4: Inspect the DataFrame
print(df.head())
print(df.info())

# Step 5: Close the connection
conn.close()
