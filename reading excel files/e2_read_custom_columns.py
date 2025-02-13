from openpyxl import load_workbook

# Load an Excel workbook
wb = load_workbook("excels/sample_data.xlsx")
sheet = wb.active  # Get the first sheet

# Read only Column 1 and Column 3 (assuming they are A and C)
for row in sheet.iter_rows(min_row=2, values_only=True):
    print(f"Column 1: {row[0]}, Column 3: {row[2]}")

# sheet has following data: Product, Sales, Category

# List all Products
product_list = []
for row in sheet.iter_rows(min_row=2, max_row=6, values_only=True):
    product_list.append(row[0])

# make all products unique
product_list = set(product_list)
print(product_list)
