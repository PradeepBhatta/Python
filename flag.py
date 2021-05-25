
# PROGRAM TO PRINT NEPAL'S FLAG USING TIME MODULE

import time

for i in range(10):
    for j in range(i):
        print("*",end="")
        time.sleep(0.01)
    print("")
    time.sleep(0.01)
    
for i in range(10):
    for j in range(i+2):
        print("*",end="")
        time.sleep(0.01)
    print("")
    time.sleep(0.01)

for k in range(5):
    print("*")
    time.sleep(0.01)
    
