def three_sum(arr):
    dict_arr = dict()
    for c in arr:
        dict_arr[c] = c

    for a in arr:
        for b in arr:
            if (-a-b) in dict_arr:
                print(a,b, (-a-b))
                return True


arr = [2,3,-1]
print(three_sum(arr))