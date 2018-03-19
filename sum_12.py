#
# def sum_two_num_to_twelve(lst):
#     print("")
#     dict_lst = dict()
#     new_lst = list()
#     for item in lst:
#         dict_lst[item] = item
#         new_lst.append(12-item)
#     print(new_lst)
#     for item in new_lst:
#         if item in dict_lst:
#             print(item,12-item)
#             return True
#     return False
#
#
# lst = [1,2,3,9]
# print(sum_two_num_to_twelve(lst))

#
def sum_to_twelve(arr,sum):
    dict1 = dict()
    res= dict()
    flag = False
    cnt = 0
    if sum%2==0:flag = True
    for i in arr:
        if (flag and i == sum/2):
            cnt+=1
            continue
        dict1[sum-i]=0

    if(cnt>1):
        print(sum//2,sum//2)
    for i in arr:
        if i in dict1:
            if((i,sum-i) in res or (sum-i,i) in res):
                continue
            res[(i,sum-i)]=0
            print(i,sum-i)


lst = [1,2,6,3,9,9,3,13,-1,12,0]
sum_to_twelve(lst,12)