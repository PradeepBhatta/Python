n = input("Enter a number ")
n = int(n)
a = n
s = 0
while n!= 0:
    r = n % 10
    s = s * 10 + r
    n= int(n/10)
        
if a == s :
    print("Number is palindrome")
else:
    print("Number is not palindrome")
