import sqlite3
import pandas as pd
#git push -u origin newb


# Define the SQLite database path
database_path = 'demoDb.sqlite'

# Define the path to the CSV file
csv_path = 'bloodtypes.csv'

try:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_path)
    print("CSV file successfully loaded.")
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    exit()

# Connect to the SQLite database
try:
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    print("Connected to SQLite database.")
except sqlite3.Error as e:
    print(f"Error connecting to the database: {e}")
    exit()

# Define the table name
table_name = 'bloodtypes'

# Check if the DataFrame is empty
if df.empty:
    print("The DataFrame is empty. No data to insert.")
    connection.close()
    exit()

# Create table based on the DataFrame's columns
columns = ', '.join([f'"{col}" TEXT' for col in df.columns])
create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns});'

try:
    # Execute the table creation query
    cursor.execute(create_table_query)
    print("Table created successfully or already exists.")
except sqlite3.Error as e:
    print(f"Error creating the table: {e}")
    connection.close()
    exit()

# Prepare the insertion query
insert_query = f'INSERT INTO {table_name} VALUES ({", ".join(["?"] * len(df.columns))})'

# Insert data into the SQLite table
try:
    cursor.executemany(insert_query, df.itertuples(index=False, name=None))
    connection.commit()
    print("Data inserted successfully.")
except sqlite3.Error as e:
    print(f"Error inserting data: {e}")
    connection.close()
    exit()

# Retrieve data from the table to verify insertion
try:
    cursor.execute(f'SELECT * FROM {table_name}')
    rows = cursor.fetchall()
    print("Retrieved data from the table:")
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print(f"Error retrieving data: {e}")

# Close the connection
connection.close()
print("Connection closed.")
