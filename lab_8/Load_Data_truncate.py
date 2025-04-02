import duckdb
import pandas as pd

# Define the database path
cpi_database = r"C:\Advanced-computing-in-context\alexa_ijaz_krishna\lab_8\cpi_database.duckdb"

# Connect to DuckDB
con = duckdb.connect(cpi_database)

# Load new dataset
csv_25 = r"C:\Advanced-computing-in-context\alexa_ijaz_krishna\lab_8\PCPI25M2.csv"
df_new = pd.read_csv(csv_25)

# Truncate the table (delete all existing data)
con.execute("DELETE FROM cpi_trunc")

# Insert new data
con.execute("INSERT INTO cpi_trunc SELECT * FROM df_new")

# Verify row count after truncation and load
print("Rows in cpi_trunc after truncate and load:", con.execute("SELECT COUNT(*) FROM cpi_trunc").fetchall())

# Close connection
con.close()


## cpi_trunc table now only contain data from PCPI25M2.csv.