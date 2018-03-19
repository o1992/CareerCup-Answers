import math
from collections import deque
def str_sum(str1,str2):
    len1 = len(str1)
    len2 = len(str2)

    prefix = int(math.fabs(len1-len2))
    if(len1>len2):
        str2 = "0"*(prefix) +str2
    if(len2>len1):
        str1 = "0"*(prefix) + str1
    sum_str = deque()
    buff = 0
    tmp_sum = 0
    for i in range(len(str1)-1,-1,-1):
        sum = buff + int(str1[i]) + int(str2[i])
        if(sum>9):
            sum_str.appendleft(sum%10)

            buff = 1
        else:
            sum_str.appendleft(sum)
            buff = 0
    if(buff==1):
        sum_str.appendleft(buff)
    res_str = ""
    zer_flag = True
    for i in sum_str:
        if(zer_flag==True):
            if i ==0:
                continue
            else:
                zer_flag = False

        res_str+=str(i)
    if (len(res_str)==0):
        res_str = "0"
    print(res_str)



str_sum("001","99999999999999999999999999")