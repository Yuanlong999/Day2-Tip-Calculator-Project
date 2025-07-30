print("Welcome to the tip calculator!")

bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

bill_float = float(bill)
tip_percent = int(tip) / 100
people_int = int(people)

total_tip = bill_float * tip_percent
total_bill = bill_float + total_tip
split_amount = total_bill / people_int

final_amount = round(split_amount, 2)

print("Each person should pay: $" + str(final_amount))
