n=int(input("enter a number"))
num=n
rev=0
while(num>0):
    d=num%10
    rev=rev*10+d
    num=num//10
if rev==n:
    print(n,"is palindrome")
else:
    print(n,"is not palindrome")
    