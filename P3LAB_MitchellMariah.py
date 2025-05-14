#Mariah Mitchell
#23 April 2025
#P3LAB
#Programming money (float) Values
import math

# Enter money as a float
money = float(input("Enter the amount of money as a float: $"))

total_cents = int(money * 100)

#Calculate whole dollar
dollars = total_cents // 100
if dollars <= 1: print(f"{dollars} Dollar")
else: print(f"{dollars} Dollars")

#change dollar to dime amount
money = total_cents - (dollars * 100)
#Add dimes to money caculation
dimes = money // 10
if dimes == 1: print(f"{dimes} Dime")
else: print(f"{dimes} Dimes")



#Calculate zero money with "no change"
money = float(input("Enter the amount of money as a float: $"))
if money == 0: print("No Change")



#Calculate each type of mooney
money = float(input("Enter the amount of money as a float: $"))

total_cents = int(money * 100)

#Calculate quarter amount
quarters = total_cents // 25
if quarters >= 1: print(f"{quarters} Quarter")
else: print(f"{quarters} Quarters")

money = total_cents - (quarters * 25)

#Add dimes to calculation
dimes = money // 10
if dimes == 1: print(f"{dimes} Dime")
else: print(f"{dimes} Dimes")

money = money - (dimes * 10)

# Add nickels to calculation
nickels = money // 5
if nickels >= 1: print(f"{nickels} Nickel")
else: print(f"{nickels} Nickels")
money = money - (nickels * 5)

# Add Pennys to calculation
pennies = money // 1
if pennies >= 1: print(f"{pennies} Penny")
else: print(f"{pennies} Pennies")


