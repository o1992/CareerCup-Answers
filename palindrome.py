import itertools

def find_pair_palindrome(arr):
    arr_comb = list(itertools.combinations(arr,2))

    check_pal(arr_comb)



def check_pal(arr):
    for i in arr:
        tmp = str(i[0]+ i[1])
        tmp_rev = str(i[1] + i[0])
        if( tmp == tmp[::-1] ):
           # print(tmp)
            print(i[0], i[1])
        if(tmp_rev == tmp_rev[::-1]):
            print(i[1],i[0])



arr = ["hey", "goodbye", "none", "enon"]
find_pair_palindrome(arr)








# import itertools
#
# def find_pair_palindrome(arr):
#     sol = list()
#     reverse_arr = list()
#     for item in arr:
#         reverse_str = ""
#         for char in item:
#             reverse_str = char + reverse_str
#         reverse_arr.append(reverse_str)
#     for item in arr:
#         i = 0
#         for reverse_item in reverse_arr:
#             if  str(reverse_item).startswith(str(item)):
#                 sol.append((item, arr[i]))
#             i += 1
#
#
# arr = ["hey", "goodbye", "none", "xenon"]
# find_pair_palindrome(arr)
#


# import itertools
# from itertools import combinations
#
#
# def is_palindrome(my_dict, key_combos):
#     results = {}
#
#     for keys in key_combos:
#         phrase = my_dict[keys[0]]+my_dict[keys[1]]
#
#         if phrase == phrase[::-1]:
#             results[keys[0]] = my_dict[keys[0]]
#             results[keys[1]] = my_dict[keys[1]]
#
#     return results
#
#
# if __name__ == "__main__":
#     my_dict = {"i1": "xenonex", "i2": "xenon", "i3": "none"}
#
#     key_combo = list(combinations(my_dict.keys(), 2))
#     print(key_combo)
#     key_combo_reverse = [(i[1], i[0]) for i in key_combo]
#     key_combo.extend(key_combo_reverse)
#
#     results = is_palindrome(my_dict, key_combo)
#     print(results)