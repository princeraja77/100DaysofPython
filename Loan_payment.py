t_amount=float(input("Enter the total amount of loan\n"))
i_rate=float(input("Enter the rate of interest\n"))
emi=float(input("Enter monthly emi amount\n"))
months=int(input("Enter for how many months calculation required\n"))
for i in range(1,months+1):
    monthly_interest=(t_amount*i_rate/100)/12
    if t_amount-(emi-monthly_interest)<0:
        print(f"For month {i+1} paid {t_amount+monthly_interest} of which {monthly_interest} is interest",
           f"and owed amount is {0.00}")
        break
    t_amount-=emi-monthly_interest
    print(f"For month {i+1} paid {round(emi,2)} of which {round(monthly_interest,2)} is interest",
           f"and owed amount is {round(t_amount,2)}")