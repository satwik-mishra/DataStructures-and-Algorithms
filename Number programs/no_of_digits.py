n=int(input("enter a number"))
count=0
num=n
while(num>0):
    d=n%10
    count+=1
    num=num//10
print("number of digits in",n,"is",count)