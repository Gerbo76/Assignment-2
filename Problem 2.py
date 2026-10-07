salary = float(input("Enter annual salary: $"))
score = int(input("Enter performance score (0-100): "))
# used float for salary as there are usually decimal points involved, used int for score as
# the scale is simply 0-100 with no decimals
if score >= 90:
    bonus_rate = 0.20
elif score >= 80:
    bonus_rate = 0.10
elif score >= 70:
    bonus_rate = 0.05
else:
    bonus_rate = 0
# set rules for output using if and elif, else covers all other scores not worthy of bonus
bonus_amount = salary * bonus_rate

print(f"Performance Bonus: {bonus_rate:.0%}")
print(f"Bonus Amount: ${bonus_amount:,.2f}")
# converted bonus rate to a percentage as it is a percentage of your salary given as extra pay
# converted bonus amount to a currency format with commas and two decimal places ($65,000.67)