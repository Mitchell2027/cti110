##Mariah Mitchell
#23 April 2025
#P3HW1
#Programmming a list of grades/results


#Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
print()
print('-------------Results------------')

# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades
low = min(grades)
high = max(grades)
sum_of_grades = sum(grades)
avg = sum(grades) / len(grades)

# print results in an organized graphical display

print(f"{'Lowest grade:':<20} {(low):.2f}")
print(f"{'Highest grade:':<20} {(high):.2f}")
print(f"{'Sum of grades:':<20} {(sum_of_grades):.2f}")
print(f"{'Average:':<20} {(avg):.2f}")
print('----------------------------------------')

# determine letter grade for average

if avg >= 90:
    print('Your letter grade is: A')
elif avg >= 80:
    print('Your letter grade is: B')
elif avg >= 70:
    print('Your letter grade is: C')
elif avg >= 60:
    print('Your letter grade is: D')
else:
    print('Your letter grade is: F')


