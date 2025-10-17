products = [
{"name": "Laptop", "price": 1200, "category": "Electronics"},
{"name": "Shirt", "price": 45, "category": "Clothing"},
{"name": "Phone", "price": 800, "category": "Electronics"},
{"name": "Shoes", "price": 120, "category": "Clothing"},
{"name": "Tablet", "price": 350, "category": "Electronics"},
{"name": "Jacket", "price": 95, "category": "Clothing"},
{"name": "Book", "price": 25, "category": "Books"},
{"name": "Headphones", "price": 150, "category": "Electronics"}
]
# [] = ada array (tempat penyimpanan banyak data di satu variable saja)
# {} = menandakan baris pada array, [] seperti tabel dan {} paragraf pertama
# "" = menandakan kalau data tersebut data string, string itu seperti abjad/kalimat biasa , bukan numeric
# : = untuk pengecekan
# \n = untuk enter ke bawah
# for = untuk pengulangan
# index = 
# == fungsinya buat menandakan bahwa inputan harus sama dengan kriteria
print("===PRODUCT DISCOUNT CALCULATOR===\n")

for product in products:
    if category == "Electornics":
        if price >= 1000:
            discount_rate = 0.2
        elif price >= 500:
            discount_rate = 0.15
        else :
            discount_rate = 0.10
    elif category == "Clothing":
        if price >= 100:
            discount_rate = 0.25
        else :
            discount_rate = 0.15
    elif category == "Books":
        discount_rate = 0.10
    discount_amount = price*discount_rate
    Final_Price = price-discount_amount
print("===SUMMARY===\n")
print ("Product = {name}")
print ("Category : {} ")

    
