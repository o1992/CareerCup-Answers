def missing_range(lst):
    if (len(lst) == 0):
        return ['0-99']
    new_lst = list()
    if (lst[0] != 0):
        new_lst.append("0-" + str(lst[0] - 1))
        # print(lst)

    start = lst[0]
    end = -1

    for i in range(len(lst)):
        if (i == len(lst) - 1):
            if (lst[i] != 99):
                start = lst[i] + 1
                end = 99
                new_lst.append(str(start) + "-" + str(end))
            continue
        if (lst[i + 1] - lst[i] == 1):
            continue
        start = lst[i] + 1
        end = lst[i + 1] - 1
        if (start == end):
            new_lst.append(str(start))
        else:
            new_lst.append(str(start) + "-" + str(end))
    print(new_lst)


lst = [3, 5]
missing_range(lst)
