credit_score = int(input("Enter credit score: "))
income = float(input("Enter annual income: $"))
# credit score is set scale with no decimals so used int, income usually includes decimals so used float
# added $ to make it more obvious you should be inputting money data in dollars
if credit_score >= 720 and income >= 60000:
    risk = "Low Risk"
elif credit_score >= 650 and income >= 40000:
    risk = "Medium Risk"
else:
    risk = "High Risk"
# set rules using if and elif, else covers scores and income outside of defined ranges
# of medium and high risk
print(f"Loan Risk Category: {risk}")
