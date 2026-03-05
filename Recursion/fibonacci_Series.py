def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
x=int(input("enter a number : "))
result=fibo(x)
print(result)