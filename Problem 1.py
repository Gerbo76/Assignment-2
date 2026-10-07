purchase = float(input("Enter purchase amount: $"))
member = input("Are you a member? (yes/no): ")
# Used float as purchase amount could be a decimal and needs to be a number
if member == "yes":
    if purchase >= 100:
        discount = 0.15
    else:
        discount = 0.05
else:
    if purchase >= 150:
        discount = 0.10
    else:
        discount = 0
# Only included if member = "yes" because else statement can be used to refer to all other responses
final_price = purchase * (1 - discount)

print(f"Discount applied: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")
# converted discount applied to a percentage and final price to display two decimal points