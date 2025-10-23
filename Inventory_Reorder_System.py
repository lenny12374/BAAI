import pandas as pd

file_path = 'B2_Inventory_Reorder_System.xlsx'
data = pd.read_excel("D:/Users/User/Desktop/Inventory_Reorder_System.xlsx")

data['Reorder_Quantity'] = 0
data ['Reorder_Cost'] = 0

safety_buffer = 10

for i, row in data.iterrows():
    if row['Current_Stock'] < row['Minimum_Stock']:
        reorder_qty = (row['Minimum_Stock'] - row['Current_Stock']) + safety_buffer
        reorder_cost = reorder_qty * row['Unit_Price']
        data.at[i, 'Reorder_Quantity'] = reorder_qty
        data.at[i, 'Reorder_Cost'] = reorder_cost
reorder_products = data[data['Reorder_Quantity']>0]
good_stock_products = data[data['Reorder_Quantity']== 0]['Product_Name'].tolist()
total_reorder_cost = reorder_products['Reorder_Cost'].sum()

print("INVENTORY REORDER REPORT")
print("========================")
print("Products Needing Reorder:\n")
for _, row in reorder_products.iterrows():
    print(f"{row['Product_Name']}: Reorder {row['Reorder_Quantity']} units | Cost: ${row['Reorder_Cost']:,}")

print(f"\nTotal Reorder Cost: ${total_reorder_cost:,}")
print(f"Products in Good Stock: {', '.join(good_stock_products)}")