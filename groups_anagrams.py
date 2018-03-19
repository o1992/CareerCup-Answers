

# set = ['cars','arcs','bike','trees','steer']

# sorted_set = []
# for item in set:
#     sorted_set.append((''.join(sorted(item)),item))
#
# sorted_set.sort(key=lambda tup: tup[0])
# print(sorted_set)
#
# index_sep=list()
# start_idx = 0
# eq_check = sorted_set[0][0]
# index_sep.append(0)
# start_flag = True
# for item in sorted_set:
#     if(start_flag):
#         start_flag = False
#         continue
#     if(str(item[0]) == eq_check):
#         start_idx = start_idx + 1
#
#     else:
#         eq_check = item[0]
#         start_idx = start_idx + 1
#         index_sep.append(start_idx)
#
# print(index_sep)

set = ['cars','arcs','bike','trees','steer']
set_tup = []
dict_set = dict()
for x in set:
    sort1 = ''.join(sorted(x))
    if sort1 in dict_set:
        dict_set[sort1] +=[x]
    else:
        dict_set[sort1] = [x]
print(dict_set)