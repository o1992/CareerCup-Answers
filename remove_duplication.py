def remove_duplications(arr):
    no_dup = set(arr)
    return list(no_dup)

arr = [0,1,1,2,3,4,1,0,4]
print(remove_duplications(arr))