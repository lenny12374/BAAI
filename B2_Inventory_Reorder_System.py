# inventory_reorder.py
import pandas as pd
import os


# Baca file excel
df = pd.read_excel("D:/Users/User/Desktop/Inventory_Reoder_System.xlsx")

# Pastikan kolom yang diperlukan ada (toleransi nama kolom sederhana)
required = {"Product_Name", "Current_Stock", "Minimum_Stock", "Unit_Price"}
if not required.issubset(set(df.columns)):
    raise ValueError(f"File harus punya kolom: {required}. Kolom sekarang: {set(df.columns)}")

# Proses reorder
safety_buffer = 10
rows_need = []
good_stock = []
total_cost = 0

for _, row in df.iterrows():
    name = str(row["Product_Name"])
    cur = int(row["Current_Stock"])
    mn = int(row["Minimum_Stock"])
    price = float(row["Unit_Price"])

    if cur < mn:
        reorder_qty = (mn - cur) + safety_buffer
        cost = reorder_qty * price
        total_cost += cost
        rows_need.append({
            "Product": name,
            "Reorder_Qty": reorder_qty,
            "Cost": cost
        })
    else:
        good_stock.append(name)

# Cetak laporan
print("INVENTORY REORDER REPORT")
print("-" * 30)
print("Products Needing Reorder:\n")

if rows_need:
    for r in rows_need:
        # Format cost dengan pemisah ribuan
        cost_str = f"${r['Cost']:,.0f}"
        print(f"{r['Product']}: Reorder {r['Reorder_Qty']} units | Cost: {cost_str}")
else:
    print("None")

print("\nTotal Reorder Cost:", f"${total_cost:,.0f}")
print("Products in Good Stock:", ", ".join(good_stock) if good_stock else "None")