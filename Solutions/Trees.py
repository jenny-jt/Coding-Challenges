# Define a tree structure - start with a tree with two nodes.
# For an extra challenge, ask yourself how the implementation would
# change if there are more than two branches per node. An example of this would be a Trie.
# These are very useful for autocomplete and the like

# Tree and Node classes
class Node():
    """node in tree"""
    def __init__(self, value, children):
        self.value = value
        self.children = children or []
    
    def __repr__(self):
        return f'<Node={self.value}>'

class Tree():
    """tree class"""
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return f'<Tree={self.root}>'

node_vals = ["A", "B"]
nodes = []
for val in node_vals:
    nodes.append(Node(val))

Node_A.children.append(Node_B)

{"A":["B", "C", "D"], "B":[]}



# Write a function that returns the lowest common ancestor of two nodes.
# the lowest node in T that has both n1 and n2 as descendants

# This is a common problem, however when we master this + (depth + breadth)
# first search tree problems will become second nature as the traversal is the same
# and the only conditions that usually change are which direction you take when

def lowest_common_ancestor(node, v1, v2):
    target = [v1,v2]
    def dfs(node, target):
        if not node:
            return
        # if node is either p or q, will return node
        if node.val in target:
            return node
        # otherwise, search to left and right of node
        left = dfs(node.left, target)
        right = dfs(node.right, target)
        # p and q are in left and right branches, LCA is the node
        if left and right:
            return node
        # if only L or R branch, will find first node that is p or q (child of itself)
        return left or right
    return dfs(root, target)


#Instead of 2 nodes, what if we had a list of nodes.
def challenge_lowest_common_ancestor(node, alon):
        alon = [v1,v2, v3, v4]

    def dfs(node, target, children):
        if not node:
            return
        # if node is in alon, will return node
        if node.val in alon:
            return node
        # otherwise, search children of node
        for child in node.children:
            child_found = dfs(child, target)
            if child_found:
                children.append(child_found)
        
        if len(children) == len(alon):
            return node
    
    return dfs(root, target, [])


class Node():
    """node in tree"""
    def __init__(self, value, children):
        self.value = value
        self.children = children or []
    
    def __repr__(self):
        return f'<Node={self.value}>'

class Tree():
    """tree class"""
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return f'<Tree={self.root}>'
    
                1
            2         3
        4       5
        
   
6 8 
        
   3 5     
            1
         3      2
      6      5     4
          8    9
            
        # node.right, add that value to an existing ds
        # reach leaf node(right is none) stop     
        # result = [7, 17, 14]
        # d = {1:3, 2:5, 4:none, 3:6, 5:8, 6:none, 8:none, 9:none}
        
def diagonal_sum():    
    """given binary tree, calculate diagonal sum"""
    arr = []
    # start at root
    # store node.left in q
    # sum node.right
    
    if node.right:
        # add all node.rights until reach leaf
        dfs(node, arr)

    q.pop()
        
        
def invert_tree(node):
    """given binary tree, invert the tree"""
    # start at root
    if node:
        temp = node.left
        node.left = node.right
        node.right = temp
    
    dfs(node.left)
    dfs(node.right)
    
    return node


