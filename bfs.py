from collections import deque

class node():
    value = None
    left_child = None
    right_child = None
    def __repr__(self):
        return str(self.value**2)

    def __init__(self, val):
        self.value = val


class bin_tree():
    root = node(6)
    root.left_child = node(3)
    root.left_child.right_child = node(3)
    root.left_child.right_child.right_child = node(3)
    root.left_child.right_child.right_child.left_child =  node(3)
    root.left_child.right_child.right_child.left_child.right_child = node(5)
    root.left_child.right_child.right_child.left_child.right_child = node(5)
    root.left_child.right_child.right_child.left_child.right_child.left_child = node(150)

    root.right_child = node(10)
    root.right_child.right_child = node(20)
    root.right_child.left_child = node(8)
    root.right_child.left_child.right_child = node(10)
    root.right_child.left_child.right_child.right_child = node(10)
    root.right_child.left_child.right_child.right_child.left_child = node(150)


def search_bfs_shortestpath(deq,val):
    if(len(deq)==0):
        return -1

    node,depth = deq.popleft()
    if(node.value == val):
        return depth
    if(node.left_child != None):
        deq.append((node.left_child,depth+1))
    if(node.right_child != None):
        deq.append((node.right_child,depth+1))
    return search_bfs_shortestpath(deq,val)



nd_class = bin_tree()
max = [[0,nd_class.root]]
q = deque()
q.append((nd_class.root,0))
print(search_bfs_shortestpath(q,150))
