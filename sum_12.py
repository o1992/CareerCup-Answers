
def sum_two_num_to_twelve(lst):
    print("")
    dict_lst = dict()
    new_lst = list()
    for item in lst:
        dict_lst[item] = item
        new_lst.append(12-item)
    print(new_lst)
    for item in new_lst:
        if item in dict_lst:
            print(item)
            return True
    return False


lst = [1,2,3,4]
print(sum_two_num_to_twelve(lst))