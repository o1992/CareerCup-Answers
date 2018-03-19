# import math
#
# def print_bst(depth):
#     bst = []
#     series = [i for i in range(depth+1)]
#     calc_spaces = lambda x: int(math.pow(2, x)) - 1
#     spaces = list(map(calc_spaces, series))
#
#     current_depth = depth
#     while current_depth > 0:
#         elements = ["*" for i in range( int(math.pow(2, current_depth)) , int(math.pow(2, current_depth+1)))]
#         bst.append(elements)
#         current_depth -= 1
#     bst.append(["*"])
#     bst.reverse()
#
#     result = []
#     current_depth = depth
#     while current_depth > 0:
#         line = " " * spaces[depth - current_depth]
#         for current_element in bst[current_depth]:
#             line += str(current_element) + " " * spaces[depth - current_depth + 1]
#         result.append(line)
#         current_depth -= 1
#     result.reverse()
#
#     print(" " * spaces[depth] + "*")
#     for line in result:
#         print(line)
#
# if __name__ == "__main__":
#     print_bst(3)



def print_bst(depth):
    bst = []
    series = [i for i in range(depth+1)]
    func = lambda x:(2**x )- 1
    spaces = list(map(func,series))

    # nodes

    cur_depth = depth
    while(cur_depth>0):
        nodes = ["*" for i in range(2**cur_depth,2**(cur_depth+1))]
        bst.append(nodes)
        cur_depth-=1
    bst.append(["*"])
    bst.reverse()
    res = []
    cur_depth = depth
    while(cur_depth>0):
        line = " " * spaces[depth - cur_depth]
        for i in bst[cur_depth]:
            line+= str(i) + " "*spaces[depth- cur_depth+1]
        res.append(line)
        cur_depth-=1

    res.reverse()
    print(" " * spaces[depth] + "*")
    for i in res:
        print(i)


print_bst(3)