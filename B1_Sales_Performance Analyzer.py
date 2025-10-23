#
# Lenny,2025/10/23
# file : B1_Sales_Performance_Analyzer
# Identify top-performing sales

# 1. Input
import pandas as pd
import numpy as np

#membaca file excel
file_path = 'sales_data.xlsx'
data = pd.read_excel("D:/Users/User/Documents/sales_data.xlsx")

#menentukan apakah target tercapai
data['Target_Met'] = data['Monthly_Sales']>=data['Sales_Target']

#menghitung bonus langsung tanpa fungsi
data['Bonus'] = np.where(data['Target_Met'],data['Monthly_Sales']*0.10,data['Monthly_Sales']*0.05) 

#Membuat laporan

print("SALES PERFORMANCE REPORT")
print("=============================")
total_bonus = 0
for _,row in data.iterrows():
    status = "Target Met" if row ['Target_Met'] else "Target NOT MET"
    print(f"{row['Employee_Name']}: {status}| sales:${row['Monthly_Sales']:,}| Bonus : ${row['Bonus']:,}")
    total_bonus +=row['Bonus']
print(f"\nTotal Bonuses to Pay : ${total_bonus:,.0f}")    

