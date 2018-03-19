def print_substr(string):
    strset = dict()
    lst = list()
    for cnt in range(0,len(string)):
        for frm in range(0,len(string)):
            to=frm+cnt+1
            if to <= len(string):
                strset[string[frm:to]]=0.0
                lst.append(string[frm:to])

    for substr,dummy in strset.items():
         print(substr)
    print("$$")
    for item in lst:
        print(item)

str = "10123"



print_substr(str)