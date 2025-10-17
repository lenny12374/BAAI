#
# Lenny,2025/10/17
# file : G14460764_Lenny_Mini_Project.py
# Product Discount Calculator
#

 # 1. Input
products=[{"name":"Laptop","price": 1200, "category": "Electronics"},
          {"name":"Shirt","price": 45, "category": "Clothing"},
          {"name":"Phone","price": 800, "category": "Electronics"},
          {"name":"Shoes","price": 120, "category": "Clothing"},
          {"name":"Tablet","price": 350, "category": "Electronics"},
          {"name":"Jacket","price": 95, "category": "Clothing"},
          {"name":"Book","price": 25, "category": "Books"},
          {"name":"Headphones","price": 150, "category": "Electronics"},
          ]

# 2. Process

total_product=0
total_original=0
total_discount_amount=0
total_final=0

highest_discount_amount=[]
overall_discount_rate=[]

ele_cat=0
clo_cat=0
book_cat=0
after_disc=[]

print(f"=== PRODUCT DISCOUNT CALCULATOR ===\n")

for p in products:
  name=p["name"]
  price=p["price"]
  category=p["category"]
  original_price=float(price)
  if category=="Electronics":
    ele_cat+=1
    if price>=1000:
      discount_rate=0.2
    elif price>=500:
      discount_rate=0.15
    else:
      discount_rate=0.1
  elif category=="Clothing":
    clo_cat+=1
    if price>=100:
      discount_rate=0.25
    else:
      discount_rate=0.15
  elif category=="Books":
      book_cat+=1
      discount_rate=0.1
  else:
      discount_rate=0
  discounted_price=float(price*discount_rate)
  final_price=float(original_price-discounted_price)

  total_product+=1
  total_original+=original_price
  total_discount_amount+=discounted_price
  total_final+=final_price

  highest_discount_amount.append({"name": name, "discounted_price": discounted_price})
  overall_discount_rate.append(discount_rate)

  after_disc.append({"name": name, "final_price": final_price})

# 3. Output

  if discount_rate >=0.2:
    print(f"Product: {name} (Clearance)")
  else:
    print(f"Product: {name}")
  print(f"  Category: {category}")
  print(f"  Original Price: ${original_price:.2f}")
  print(f"  Discount Rate: {discount_rate*100:.0f}%")
  print(f"  Final Price: ${final_price:.2f}")
  print(f"  You Save: ${discounted_price:.2f}\n")

print(f"=== SUMMARY ===\n")
print(f"Total Products: {total_product:.0f}")
print(f"Total Original Price: ${total_original:.2f}")
print(f"Total Discount: ${total_discount_amount:.2f}")
print(f"Total Final Price: ${total_final:.2f}\n")

print(f"Level 1:")
highest_discount_amount = max(highest_discount_amount, key=lambda k: k["discounted_price"])
print(f"Highest Discount Amount: {highest_discount_amount['name']} (${highest_discount_amount['discounted_price']:.2f})")
print(f"Average Discount Rate: {(sum(overall_discount_rate)/total_product)*100:.0f}%\n")

print(f"Level 2:")
print(f"Category:\n  Electric={ele_cat}\n  Clothing={clo_cat}\n  Books={book_cat}")
most_expensive_product = max(after_disc, key=lambda k: k["final_price"])
print(f"Most Expensive Product: {most_expensive_product['name']} (${most_expensive_product['final_price']:.2f})")
cheapest_product = min(after_disc, key=lambda k: k["final_price"])
print(f"Cheapest Product: {cheapest_product['name']} (${cheapest_product['final_price']:.2f})\n")

print(f"Level 3:")
print(f"Total Savings: ${total_discount_amount:.2f}")