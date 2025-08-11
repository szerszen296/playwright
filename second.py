import pandas as pd
import openpyxl

df = pd.read_excel("GPUPrice_Perf.xlsx", sheet_name="Sheet1")

print(df)
