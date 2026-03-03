n=int(input("enter a number"))
rev=0
num=n
while(num>0):
    d=num%10
    rev=rev*10+d
    num=num//10
print("reverse of",n,"is",rev)