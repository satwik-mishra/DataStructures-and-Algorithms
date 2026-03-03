n=int(input("Enter a number"))
num=n
result=0
nod=len(str(num))
while(num!=0):
    d=num%10
    result=result+(d**nod)
    num//=10
if result==n:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")