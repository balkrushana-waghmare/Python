"""
Problem Statement:Write a Python program to display the current date and time.
Expected Output:
Current date and time :
2014-07-05 14:34:14
"""

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


#try 1:
# logic: wasn't aware of datetime module. took help from solution
# output: as expected
