def check_pal(str1,k):

    if str1[0] == str1[-1]:
        if len(str1) == 2: return True
        if len(str1) == 1: return True
        return check_pal(str1[1:-1],k)
    else:
        if(k==0): return False

        return check_pal(str1[1:],k-1) or check_pal(str1[:-1],k-1)








flag = check_pal("hellodpypholleh",2)
print(flag)