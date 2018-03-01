import heapq
import math


def find_nsmallest(arr,k):
   return heapq.nsmallest(2,arr)

def euclid(arr,k):
   # dist = list()
    dct= dict()
    for item in arr:
        euc=((item[0] - 5)**2 + (item[1] - 5)**2)**0.5
      #  dist.append(euc)
        dct[euc]=item
    #print(dct.keys())
    sm = (find_nsmallest(dct.keys(),k))
    for i in sm:
        print(dct[i])

euclid([(-2,-4),(0,0),(10,15),(5,6),(7,8),(-10,-30),],2)