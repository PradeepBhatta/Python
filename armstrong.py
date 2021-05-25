n = input("Enter a number ")
n = int(n)
a = n
s = 0
while n!= 0:
    r = n % 10
    s = s + r**3
    n= int(n/10)
        
if a == s :
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
