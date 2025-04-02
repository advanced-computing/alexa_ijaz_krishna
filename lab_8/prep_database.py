import duckdb
import pandas as pd

# Define database path
cpi_database = r"C:\Advanced-computing-in-context\alexa_ijaz_krishna\lab_8\cpi_database.duckdb"

# Connect to DuckDB
con = duckdb.connect(cpi_database)

# Load initial dataset
csv_24 = r"C:\Advanced-computing-in-context\alexa_ijaz_krishna\lab_8\PCPI24M1.csv"
df = pd.read_csv(csv_24)

# Create three tables: cpi_append, cpi_trunc, cpi_inc (initially same structure)
con.execute("CREATE OR REPLACE TABLE cpi_append AS SELECT * FROM df")
con.execute("CREATE OR REPLACE TABLE cpi_trunc AS SELECT * FROM df")
con.execute("CREATE OR REPLACE TABLE cpi_inc AS SELECT * FROM df")

# Verify tables created
print(con.execute("SELECT COUNT(*) FROM cpi_append").fetchall())

# Close connection
con.close()