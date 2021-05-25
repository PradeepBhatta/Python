"""
Program to print the following series

*
**
***
****
*****

"""

for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print("")
    
####################################

"""
Program to print the following series

*****
****
***
**
*

"""
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print("")
