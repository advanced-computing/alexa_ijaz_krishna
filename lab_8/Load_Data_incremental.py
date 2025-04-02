import duckdb
import pandas as pd

# Define the database path
cpi_database = r"C:\Advanced-computing-in-context\alexa_ijaz_krishna\lab_8\cpi_database.duckdb"

# Connect to DuckDB
con = duckdb.connect(cpi_database)

# Load new dataset
csv_25 = r"C:\Advanced-computing-in-context\alexa_ijaz_krishna\lab_8\PCPI25M2.csv"
df_new = pd.read_csv(csv_25)

# Check if the table exists
try:
    con.execute("SELECT COUNT(*) FROM cpi_inc")
    print("Table 'cpi_inc' exists.")
except duckdb.CatalogException:
    print("Table 'cpi_inc' does not exist. Creating the table.")
    # Create the table if it doesn't exist
    con.execute("CREATE TABLE cpi_inc AS SELECT * FROM df_new")

# Insert only new rows based on the DATE column, avoiding duplicates
con.execute("""
    INSERT INTO cpi_inc
    SELECT * FROM df_new
    WHERE NOT EXISTS (
        SELECT 1 FROM cpi_inc WHERE cpi_inc.DATE = df_new.DATE
    )
""")

# Verify the row count after the incremental load
print("Rows in cpi_inc after incremental load:", con.execute("SELECT COUNT(*) FROM cpi_inc").fetchall())

# Close the connection
con.close()
