print("Welome to the tip calculator")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

amount_of_people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill

pay_sum = "{:.2f}".format(bill_with_tip / amount_of_people, 2)

print(f"Each person should pay: ${pay_sum}")