def subsets(str_arr):
    print("")
    if len(str_arr) <= 1:
        yield str_arr
        yield []
    else:
        for item in subsets(str_arr[1:]):
            yield [str_arr[0]] + item
            yield item


str = "rrum"
dict1 = dict()
str_arr = list(str)
new_arr = list()
for i in str:
    if i not in dict1:
        new_arr.append(i)
        dict1[i]=0
gen = subsets(new_arr)
for i in gen:
    if (len(i) == 0): continue

    print(i)