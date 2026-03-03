#  BRUTE FORCE 

# n=int(input("enter a number"))
# result=[]
# for i in range(1,n+1):
#     if n%i==0:
#         result.append(i)
# print(result)


#  BETTER APPROACH (ITERATE TILL HALF OF THE NUMBER)

# n=int(input("enter a number : "))
# result=[]
# for i in range(1,n//2):
#     if n%i==0:
#         result.append(i)
# result.append(n)
# print(result)

#  OPTIMAL APPROACH (ITERATE TILL SQRT)
from math import sqrt
n=int(input("enter a number : "))
result=[]
for i in range(1,int(sqrt(n))+1):
    if n%i==0:
        result.append(i)
        if n//i!=i:
            result.append(n//i)
result.sort()
print(result)