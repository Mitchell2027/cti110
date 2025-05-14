#Mariah Mitchell
#24 April 2025
#P3HW2
#Programmed hourly pay and overtime calculations


#Employee, hours, and pay data
employee_name = input("Enter the employee's name: ")
hours_worked = float(input(f"Enter number of hours worked: "))
pay_rate = float(input(f"Enter employee's pay rate: "))
print("----------------------------------")

#Calculate the amount of pay and hours
overtime_hours = 0
overtime_pay = 0
regular_hours = hours_worked
regular_pay = regular_hours * pay_rate

#Calculate overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40  
    regular_pay = regular_hours * pay_rate
    
#Calculations for 1.5 hours overtime hours
overtime_pay = overtime_hours * (pay_rate * 1.5)

#Total Gross Pay
gross_pay = regular_pay + overtime_pay

#Output of Employee Data
print(f"Employee name:  {employee_name}")
print ('')
#Table Output
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<12}")
print("------------------------------------------------------------------------------")
print(f"{hours_worked:<15} {pay_rate:<12}{overtime_hours:<12} {overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<12.2f}")
