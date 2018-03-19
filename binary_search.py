class node():
    value = None
    left_child = None
    right_child = None

    def __init__(self, val):
        self.value = val


class bin_tree():
    root = node(6)
    root.left_child = node(3)
    root.right_child = node(10)
    root.right_child.right_child = node(20)
    root.right_child.left_child = node(8)

def search_binary_tree(root,val):
    if( root.value == val):
        return True
    if(root.left_child != None):
        if(root.value>val):
            return search_binary_tree(root.left_child,val)
    if(root.right_child != None):
        if(root.value<val):
            return search_binary_tree(root.right_child,val)
    return False


nd_class = bin_tree()
print(search_binary_tree(nd_class.root,9))





#
#
# def binary_tree(node,lst,position,height):
#     if(node == None):
#         return
#     lst.append((position,height,node.value))
#     binary_tree(node.left_child,lst,position-1,height-1)
#     binary_tree(node.right_child,lst,position+1,height-1)
#
#
#
#
# position = 0
# nd_class = bin_tree()
#
# root = nd_class.root
# lst = list()
# binary_tree(root,lst,position,0)
# lst.sort(key = lambda tup:tup[1],reverse=True)
# lst.sort(key = lambda tup:tup[0])
#
# print([x[2] for x in lst])