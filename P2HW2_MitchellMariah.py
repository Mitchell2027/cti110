#Mariah Mitchell
#3 May 2025
#P4HW1
#Programmming a list of grades/results

#Creating list to input grades
grades = []
grades.append(float(input("Enter the grade for Module 1: ")))
grades.append(float(input("Enter the grade for Module 2: ")))
grades.append(float(input("Enter the grade for Module 3: ")))
grades.append(float(input("Enter the grade for Module 4: ")))
grades.append(float(input("Enter the grade for Module 5: ")))
grades.append(float(input("Enter the grade for Module 6: ")))

#Results of lowest, highest, sum, and average
print()
print('------------Results------------')
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

print(f"Lowest grade: {lowest_grade}")
print(f"Highest grade: {highest_grade}")
print(f"Sum of grades: {sum_of_grades}")
print(f"Average grade: {average_grade:.2f}")
print('---------------------------------------')
