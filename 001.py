"""
Problem Statement: Write a Python program to print the following string in a specific format (see the output)
Expected Output: 
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""

from unittest import expectedFailure


print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")   		
print("\t\tLike a diamond in the sky.") 
print("Twinkle, twinkle, little star,") 
print("\tHow I wonder what you are")


# Try 1:
# logic: use \n at the end of the line for next line.  \t for tab
# output: not as expected

# Try 1:
# logic: remove \n from the end of the lines
# output: as expected