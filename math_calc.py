# Feb On-site Google
#
# Print all numbers satisfying the expression 2^i * 5^i
# (where i, j are integers i >= 0 and j >= 0) in increasing order up to a given bound N.
# 2^i stands for power(2, i).

import heapq,math
def calc(bound_n):
    heap = []
    log_5_n = int(math.log(n,5))
    log_2_n = int(math.log(n,2))
    c1 = 1
    c2 = 1
    i =0
    j = 0

    while(i<=log_2_n+1):

        while(j<=log_5_n+1):

            c3 = c1 * c2
            if (c3 <= n):
                heapq.heappush(heap, c3)
            c2 = c2 * 5
            j+=1

        c1 = c1 * 2
        c2=1
        j=0
        i+=1
    for i in range(len(heap)):
        yield heapq.heappop(heap)

n=10000
x = calc(n)

for i in x:
    print(i)