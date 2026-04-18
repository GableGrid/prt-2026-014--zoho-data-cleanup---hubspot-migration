import pandas as pd
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "CrossRef_DataHealth_Report.xlsx")

xls = pd.ExcelFile(file_path)
print(xls.sheet_names)