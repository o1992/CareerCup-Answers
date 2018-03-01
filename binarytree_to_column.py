class node():
    value = None
    left_child = None
    right_child = None

    def __init__(self, val):
        self.value = val


class bin_tree():
    root = node(6)
    root.left_child = node(3)
    root.left_child.right_child = node(1)
    root.left_child.left_child = node(5)
    root.left_child.left_child.right_child = node(2)
    root.left_child.left_child.right_child.right_child = node(7)
    root.left_child.left_child.left_child = node(9)
    root.right_child = node(4)
    root.right_child.right_child = node(0)
    root.right_child.right_child.left_child = node(8)


def binary_tree(node,lst,position,height):
    if(node == None):
        return
    lst.append((position,height,node.value))
    binary_tree(node.left_child,lst,position-1,height-1)
    binary_tree(node.right_child,lst,position+1,height-1)




position = 0
nd_class = bin_tree()

root = nd_class.root
lst = list()
binary_tree(root,lst,position,0)
lst.sort(key = lambda tup:tup[1],reverse=True)
lst.sort(key = lambda tup:tup[0])

print([x[2] for x in lst])