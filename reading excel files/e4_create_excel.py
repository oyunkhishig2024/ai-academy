
import openpyxl

# Create a new Excel workbook with sample data

sample_data = {
    "Sales Data A": [
        ["Product", "Sales", "Tax", "Total"],
        ["Apple", 100, 10, 110],
        ["Orange", 150, 15, 165]
    ],
    "Sales Data B": [
        ["Product", "Sales", "Tax", "Total"],
        ["Apple", 200, 20, 220],
        ["Orange", 250, 25, 275]
    ]
}

wb = openpyxl.Workbook()  #shine excel uusgej bn

for sheet_name, rows in sample_data.items():
    sheet = wb.create_sheet(title=sheet_name)
    for row in rows:
        sheet.append(row)

wb.save("outputs/sample_excel1.xlsx")
print("Excel file created successfully.")
