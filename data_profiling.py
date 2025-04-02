import pandas as pd
from ydata_profiling import ProfileReport

# Load the CSV file
file_path = "NYPD_Hate_Crimes_20250131.csv"  # Ensure it's in the same directory
df = pd.read_csv(file_path)

# Generate profiling report
profile = ProfileReport(df, title="NYPD Hate Crimes Data Report", explorative=True)
profile.to_file("data_profile_report.html")

print("Profiling complete. Open 'data_profile_report.html' in a browser.")
