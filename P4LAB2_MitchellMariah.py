# Mariah Mitchell
# P4LAB2
# 3 May, 2025
# Create a program using loops to display positive multiplication tables


run_again = 'yes'

while run_again != "no":
#Determine if the integer is positive
    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
#Display multiplication for that value from range (1-12)
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
#Negative numbers are not accepted
    else:
        print("This program does not handle negative number")
#Ask to run the program again
    run_again = input("Would you like to run the program again? ")
    
#If user enter 'no', loop is broken
print("Exiting program...")
