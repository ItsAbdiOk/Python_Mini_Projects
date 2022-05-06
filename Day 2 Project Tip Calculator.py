print("Welcome to the tip calculator")
Total_Bill = float(input("What was the total bill? $" ))
Tip_Percentage = int(input("What percentage tip would you like to give? 10, 12,or 15? "))
Num_people = int(input("How many people to split the bill?"))

Total_Tip = Total_Bill*(Tip_Percentage /100)
Tip_Per_Person = round(Total_Tip/Num_people,2)
Total_Per_Person = round((Total_Bill/Num_people) + Tip_Per_Person,2)

print(f"Each person should pay : ${Total_Per_Person}")