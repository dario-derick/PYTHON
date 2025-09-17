def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Ask user for input

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price

final_price = calculate_discount(price, discount_percent)

# Print result

if final_price == price:
    print(f"No discount applied. Final price is: {final_price}")
else:
    print(f"Discount applied! Final price is: {final_price}")
