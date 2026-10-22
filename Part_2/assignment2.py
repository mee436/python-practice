product_1 = float(input("Enter price of product 1: "))
product_2 = float(input("Enter price of product 2: "))
product_3 = float(input("Enter price of product 3: "))

total_bill_amt = product_1 + product_2 + product_3

avg_price = total_bill_amt / 3

print("Total Bill Amount: ", total_bill_amt)
print("Average Price: ", avg_price)

superhero_name = input("Enter your superhero name: ")

print(superhero_name.lower().startswith('s'))