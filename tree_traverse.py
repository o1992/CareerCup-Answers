from collections import deque
class node():
    value = None
    left_child = None
    right_child = None

    def __init__(self, val):
        self.value = val


class bin_tree():
    root = node(1)
    root.left_child = node(2)
    root.right_child = node(3)
    root.left_child.left_child = node(4)
    root.left_child.right_child = node(5)

# root = Node(1)
# root.left      = Node(2)
# root.right     = Node(3)
# root.left.left  = Node(4)
# root.left.right  = Node(5)

def preorder(node):
    if(node == None):
        return


    preorder(node.left_child)
    preorder(node.right_child)
    print(node.value)


def bfs(node):
    queue_nodes = deque()
    if(node != None):
        queue_nodes.append(node)
    while(len(queue_nodes)>0):
        node = queue_nodes.popleft()
        print(node.value)
        if(node.left_child!=None):
            queue_nodes.append(node.left_child)
        if (node.right_child != None):
            queue_nodes.append(node.right_child)

num = int(1).bit_length()
nd_tree = bin_tree()

#preorder(nd_tree.root)
bfs(nd_tree.root)
