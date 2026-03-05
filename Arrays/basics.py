# METHOD 1  - USING ARRAY MODULE

# import array
# val=array.array('i',[1,2,3,4,5,6,7])
# for i in range(0,7):
#     print(val[i],end='')
# for x in val:
#     print(x,end=" ")
 
# METHOD 2 - USING NUMPY

from numpy import *
val=array([1,2,3,4,5])
for x in val:
    print(x)

