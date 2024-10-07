print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_percentage=tip/100
tot_bill=bill+(bill*tip_percentage)
each_bill=tot_bill/people
print(f"Each person should pay: {each_bill:.2f}")
