#  ITERATIVE METHOD

# n=int(input("enter a number : "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+(i**3)
# print(sum)

#  RECURSIVE METHOD

def sum_of_nos(n):
    if n==0:
        return 0
    return (n**3) + sum_of_nos(n-1)
result=sum_of_nos(5)
print(result)
