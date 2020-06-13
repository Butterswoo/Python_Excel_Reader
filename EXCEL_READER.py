import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_excel('cars.xlsx')

verbatim = df[df['Verb English'].str.lower().str.contains('i think', na = False)]['Verb English']
print(verbatim)
# stored = verbatim.to_excel('verbatim.xlsx')
