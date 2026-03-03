#Implementing the Euclidean Algorithm (Manual Method)
a=int(input("enter a number"))
b=int(input("enter another number"))
while(b>0):
    r=a%b
    a=b
    b=r
GCD=a
print("gcd is",GCD)