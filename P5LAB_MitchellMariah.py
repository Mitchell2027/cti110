#Mariah Mitchell
#P5LAB
#7 May 2025
#Import Random Money Calculation of a self-checkout using loop
import random

def disperse_change(extra_cash):
    extra_cash = round(extra_cash, 2)
    
    #Dollars
    dollars = int(extra_cash)
    extra_cash = extra_cash - dollars
    #Cents
    quarters = int(extra_cash // 0.25)
    extra_cash = extra_cash - quarters * .25
    #Dimes
    dimes = int(extra_cash // 0.10)
    extra_cash = extra_cash - dimes * .10
    #Nickels
    nickels = int(extra_cash // 0.05)
    extra_cash = extra_cash - nickels * .05
    #Pennies
    pennies = int(extra_cash // 0.01)
    extra_cash = extra_cash - pennies * .01

    #Displays the amount of money need
    if (extra_cash == 0):
        print('No change')
    
    if dollars > 1:
        print(dollars,'Dollars')
    if dollars == 1:
        print(dollars,'Dollar')
    
    if quarters > 1:
        print(quarters,'Quarters')
    if quarters == 1:
        print(quarters,'Quarter')
        
    if dimes > 1:
        print(dimes, 'Dimes')
    if dimes == 1:
        print(dimes, 'Dime')
        
    if nickels > 1:
        print(nickels, 'Nickels')
    if nickels == 1:
        print(nickels, 'Nickel')
        
    if pennies > 1:
        print(pennies, 'Pennies')
    if pennies == 1:
        print(pennies, 'Penny')
        
#Generates amount of money owed
def gathering_info():
    random_num = round(random.uniform(0.01, 100.00), 2)
    
    print(f'You owe ${random_num}')

    money_amount = float(input('How much cash will you put in the self check-out?: '))
    
    extra_cash = money_amount - random_num
    
    print(f'Change is: ${extra_cash:.2f}')
    print('')
    
    return extra_cash
#Main function
def main():
    extra_cash = gathering_info()
    disperse_change(extra_cash)

main()
