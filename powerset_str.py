def subsets(str_arr):
    print("")
    if len(str_arr) <= 1:
        yield str_arr
        yield []
    else:
        for item in subsets(str_arr[1:]):
            yield [str_arr[0]] + item
            yield item


str = "rum"

str_arr = list({x for x in str})
gen = subsets(str_arr)
for i in gen:
    if (len(i) == 0): continue

    print(i)