class node():
    value = None
    left_child = None
    right_child = None
    def __repr__(self):
        return str(self.value)

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
    root.right_child.left_child.right_child.right_child.left_child = node(30)


def search_val_dfs(node,val):
    if(node == None):
        return None
    if(node.value == val):
        return node
    val_r = search_val_dfs(node.right_child,val)

    val_l =  search_val_dfs(node.left_child,val)
    if(val_l != None):
        return val_l
    if(val_r != None):
        return val_r
    return None

def search_depth_dfs(node,depth,max_node):
    if(node == None):
        return depth -1
    depth_r = search_depth_dfs(node.right_child,depth+1,max_node)

    depth_l =  search_depth_dfs(node.left_child,depth+1,max_node)
    if(depth_l == depth) and (depth_r == depth):
        if(max_node[0][0]<depth):
            max_node.pop()
            max_node.append([depth,node])
            return depth
    if(depth_r>depth_l):
        if (max_node[0][0] < depth_r):
            max_node.pop()
            max_node.append([depth_r, node.right_child])
            return depth_r
        if (max_node[0][0] < depth_l):
            max_node.pop()
            max_node.append([depth_l, node.left_child])
            return depth_l
    return depth


nd_class = bin_tree()
max = [[0,nd_class.root]]
print(search_depth_dfs(nd_class.root,0,max))
print(max)