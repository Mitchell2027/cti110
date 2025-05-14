#Mariah Mitchell
#4 April 2025
#P2LAB1
#Using math calculation: Diameter and Circimference.
import math

#Get radius user
radius = float(input("What is the radius of the circle?: "))

#Caculate diameter, circumference, area
cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius**2)

#Display the result
print(f"The diameter of the circle {diam:.1f}")
print(f"The circumference of the circle is {cir:.2f}")
print(f"The area of the circle is {area:.3f}")
