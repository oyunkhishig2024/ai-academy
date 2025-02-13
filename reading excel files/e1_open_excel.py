from openpyxl import load_workbook

# Load an Excel workbook
wb = load_workbook("excels/sample_data.xlsx")
sheet = wb.active  # Get the first sheet

# Read data from the first few rows
for row in sheet.iter_rows(min_row=1, max_row=5, values_only=True):
    print(row)  # Prints each row as a tuple
