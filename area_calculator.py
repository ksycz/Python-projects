"""
Area Calculator
"""
print("Calculator is starting...")

option = input("Enter C for Circle or T for Triangle: ")

if option.upper() == "C":
    radius = float(input("Enter a radius: "))
    area = 3.14159 * radius**2
    print("Area: %f" % area)
elif option.upper() == "T":
    base = float(input("Enter base: "))
    height = float(input("Enter height "))
    area = 0.5 * base * height
    print("Area: %f" % area)
else:
    print("Error! Invalid data. Please enter C for Circle or T for Triangle: ")

print("Calculator is closing...")