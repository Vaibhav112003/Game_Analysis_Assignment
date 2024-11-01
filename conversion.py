import pandas  as pd

# Load the Excel file with the correct engine
excel_file_path = 'first_dataset.xls'
output_csv_path = 'first_dataset.csv'

# Specify the engine
df = pd.read_excel(excel_file_path, engine='xlrd')  # Use 'openpyxl' if it's a .xlsx file

# Convert to CSV
df.to_csv(output_csv_path, index=False)

print("Conversion complete. Saved as", output_csv_path)
