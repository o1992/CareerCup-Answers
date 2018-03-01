def pattern_match(str_array, pattern):
    found_str_arr = list()

    # find pattern type:
    bool_left_flag = False
    bool_right_flag = False
    if (str(pattern).startswith("*")):
        bool_left_flag = True
        pattern = pattern[1:]
    if (str(pattern).endswith("*")):
        pattern = pattern[:-1]
        bool_right_flag = True

    for item in str_array:
        check = False
        if ((not bool_left_flag) and (not bool_right_flag)):
            if (item == pattern):
                check = True
        elif (bool_left_flag and bool_right_flag):
            if pattern in item:
                check = True
        elif (bool_left_flag and (not bool_right_flag)):
            if str(item).endswith(pattern):
                check = True
        elif ((not bool_left_flag) and (bool_right_flag)):
            if str(item).startswith(pattern):
                check = True
        if (check):
            found_str_arr.append(item)
    print(found_str_arr)


pattern_match(["crane", "drain", "refrain"], "*ane")