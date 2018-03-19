

def maxSubArraySum(a, size):
    max_so_far = -100000
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

arr = [-10,1,2,5,10,-3,-4]
print(maxSubArraySum(arr,len(arr)))