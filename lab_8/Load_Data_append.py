# Load Data
import duckdb
import pandas as pd

cpi_database = r"C:\Advanced-computing-in-context\alexa_ijaz_krishna\lab_8\cpi_database.duckdb"

con = duckdb.connect(cpi_database)

# Load new dataset
csv_25 = r"C:\Advanced-computing-in-context\alexa_ijaz_krishna\lab_8\PCPI25M2.csv"
df_new = pd.read_csv(csv_25)

# Append new data to cpi_append
con.execute("INSERT INTO cpi_append SELECT * FROM df_new")

# Verify row count after append
#print("Rows in cpi_append after append load:", con.execute("SELECT COUNT(*) FROM cpi_append").fetchall())

# Close connection
con.close()

# cpi_append table will contain both old and new records. new records will simply be duplicated