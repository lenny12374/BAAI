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

print("===PRODUCT DISCOUNT CALCULATOR===\n")

total_original=0
total_discount_amount=0
total_final_price=0

for product in products:
    name = product["name"]
    category = product["category"]
    price = product["price"]

    if category == "Electronics":
        if price >= 1000:
            discount_rate = 0.2
        elif price >= 500:
            discount_rate =0.15
        else:
            discount_rate = 0.10
    elif category == "Clothing":
        if price >=100:
            discount_rate = 0.25
        else :
            discount_rate = 0.15
    elif category == "Books":
        discount_rate = 0.10
    else :
        discount_rate = 0.0

    discount_amount = price*discount_rate
    final_price = price-discount_amount

    total_original +=price
    total_discount_amount += discount_amount
    total_final_price += final_price

    print(f"Product:{name}")
    print(f"Category :{category}")
    print(f"Original Price: ${price:.2f}")
    print(f"Discount: {int(discount_rate*100)}%")
    print(f"Final Price: ${final_price:.2f}\n")

print("=== SUMMARY ===")
print(f"Total Products : {len(products)}")
print(f"Total Original Price : ${total_original:.2f}")
print(f"Total Discount: $ {total_discount_amount:.2f}")
print(f"Total Final Price: ${total_final_price:.2f}")
