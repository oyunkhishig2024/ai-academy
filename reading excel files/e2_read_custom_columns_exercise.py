import openpyxl

# Load an Excel workbook
wb = openpyxl.load_workbook("excels/sample_data.xlsx")
sheet = wb.active  # Get the first sheet
# sheet has following data: Product, Sales, Category

# List all Categories
category_list = []
for row in sheet.iter_rows(min_row=2, max_row=6, values_only=True):
    # TO DO
    pass

# make all categories unique
category_list = set(category_list)
print(category_list)

# Summarize all sales for Electronics
total_sales = 0
for row in sheet.iter_rows(min_row=2, max_row=6, values_only=True):
    # TO DO
    pass
print(f"Total sales for Electronics: {total_sales}")