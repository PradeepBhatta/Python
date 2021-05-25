"""
Program to print the following series

10 20 30 40 50  
20 30 40 50 60  
30 40 50 60 70  
40 50 60 70 80  
50 60 70 80 90  

"""

for i in range(5):
    for j in range(5):
        print((i+j+1)*10,end=" ")
    print("")
