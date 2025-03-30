def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
original_price = float(input("Enter the original price of the item: $"))
discount = float(input("Enter the discount percentage: "))

# Calculate and display the final price
final_price = calculate_discount(original_price, discount)

if final_price < original_price:
    print(f"A {discount}% discount was applied.")
    print(f"Final price after discount: ${final_price:.2f}")
else:
    print("No discount was applied since the discount percentage is less than 20%.")
    print(f"Original price: ${original_price:.2f}")
