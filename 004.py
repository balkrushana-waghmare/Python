"""
Problem Statement:  Write a Python program which accepts the radius of a circle from the user and compute the area.
Expected Output:
r = 1.1
Area = 3.8013271108436504
"""
from math import pi
r = float(input())
print("Area = ",  pi * r * r)




# try 1:
# issues: problm faced for user input in vs code
# solution: changes the setting of code runner

# try 2:
# issues: didnt get the expected result (I was using value of pi as 3.14). afterwarrds took help from solution and use math function
# output: as expected 