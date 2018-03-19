from collections import Counter
def task_scheduler(arr,cooldown):
    cooldown = cooldown+1
    cnt = Counter(arr)
    tsker = list()
    last_one = {x:-len(arr) for x in arr}
    i=0
    while(True):
        startflag = True
        for key,item in cnt.items():
            if(startflag):
                if item==0:break
                startflag = False
            if (item==0):
                continue
            delta = i-last_one[key]
            if(delta>cooldown):
                tsker.append(key)
                cnt[key]=item-1
                last_one[key] = i
            else:
                for j in range(cooldown-delta):
                    tsker.append("_")
                    i += 1


            i += 1
        if (startflag):
            break
    return tsker



str1 = "AAABBB"
arr = list(str1)
print(task_scheduler(arr,2))
