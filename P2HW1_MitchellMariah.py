#Mariah Mitchell
#12 April 2025
#P2HW1
#Calculating travel expenses

#finding the budget and destination
budget = float(input("Enter budget: "))

location = input("Enter your travel destination: ")

gas = float(input("How much do you think you will spend on gas? {:.2f}"))

accomodation = float(input("Approximately, how much will you need for accomodation/hotel? "))

food = float(input("Last, how much do you need for food? "))

#Formula
expenses = gas + accomodation + food
Total = budget - expenses

#Travel Expense List
print('------------Travel Expenses----------')
print(f'Location:           {location}')
print(f'initial Budget:     ${budget}')
print(f'Fuel:               ${gas}')
print(f'Accomodation:       ${accomodation}')
print(f'Food:               ${food}')
print('-------------------------------------')
print()
print(f'Remaining Balance:  ${Total}')
