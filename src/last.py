import pandas as pd

xls = pd.ExcelFile("contacts.xlsx")
print(xls.sheet_names)