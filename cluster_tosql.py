import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# Define the SQLite database path
database_path = 'demoDb.sqlite'

# Define the path to the CSV file
csv_path = 'clusters.csv'


# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_path)

# Connect to the SQLite database
connection = sqlite3.connect(database_path)

# Create a cursor object using the connection
cursor = connection.cursor()

# Define the table name
table_name = 'clusters'

# Dynamically create the table based on the DataFrame's columns
# Assuming all columns are of type TEXT; adjust types if needed
columns = ', '.join([f'"{col}" TEXT' for col in df.columns])
create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns});'

# Execute the table creation query
cursor.execute(create_table_query)

# Insert data into the SQLite table
# Use parameterized queries to avoid SQL injection
insert_query = f'INSERT INTO {table_name} VALUES ({", ".join(["?"] * len(df.columns))})'
cursor.executemany(insert_query, df.itertuples(index=False, name=None))

# Commit the changes to save the data
connection.commit()

# Retrieve data from the table to verify insertion (optional)
cursor.execute(f'SELECT * FROM {table_name}')
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    print(row)


# Close the connection
connection.close()

# Check the first few rows
print(table_name.head())

# Plot the data
plt.figure(figsize=(8, 5))
plt.bar(table_name["Region"], table_name["Estimate"], color=['blue', 'green'])

plt.xlabel("Region")
plt.ylabel("Estimate")
plt.title("Main Estimates from West and Scandinavia")
plt.show()
