# def merge(arr1,arr2):
#     i1=0
#     i2=0
#     c=list()
#     while(not i1==(len(arr1)) and (not i2==(len(arr2)))):
#         if(arr1[i1]<arr2[i2]):
#             c.append(arr1[i1])
#             if(i1 != len(arr1)):
#                 i1+=1
#         else:
#             c.append(arr2[i2])
#             if (i2 != len(arr2)):
#                 i2 += 1
#     if(len(arr1)==i1):
#         c.extend(arr2[i2:])
#     else:
#         c.extend(arr1[i1:])
#     return c
#
#
# def mergesort(arr):
#     if(len(arr)==0) or (len(arr)==1):
#         return arr
#     middle = (len(arr)//2)
#     a = mergesort(arr[:middle])
#     b = mergesort(arr[middle:])
#     return merge(a,b)
#
# print(mergesort([4,3,2,1,8,7,-1,0,5]))
from collections import deque

def merge(arr1,arr2):
    c = deque()
    while( (len(arr1)!= 0) and (len(arr2)!= 0)):
        if(arr1[0]<arr2[0]):
            c.append(arr1.popleft())
        else:
            c.append(arr2.popleft())
    if(len(arr1)!=0):
        c.extend(arr1)
    else:
        c.extend(arr2)


def mergesort(arr):
    if(len(arr)==0) or (len(arr)==1):
        return arr
    middle = (len(arr)//2)
    a = mergesort(arr[:middle])
    b = mergesort(arr[middle:])
    return merge(a,b)

print(mergesort(deque([4,3,2,1,8,7,-1,0,5])))