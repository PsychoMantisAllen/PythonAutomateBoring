import openpyxl
import os

wb = openpyxl.workbook()
wb
wb.get_get_sheet_names()
sheet = wb.get_get_sheet_names('Sheet')

sheet['A1'] = 42    # change the value of a cell
sheet['A2'] = 'Hello'
os.chdir()
wb.save('example.xlsx')

sheet2 = wb.create_sheet()  # create a new sheet
sheet2.title = 'New sheet name'     # change sheet name
wb.save('example.xlsx')

wb.create_sheet(index=0, title='Another one')   # alternative way to create a sheet
# index means the position of the sheet

