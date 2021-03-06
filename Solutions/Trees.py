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


# using dict
def diagonal_sum():    
    """given binary tree, calculate diagonal sum"""
    # initialize dict
    d = defaultdict(int)
    d[0] = root.val

    # traverse tree
    i = 0
    def dfs(node, d, i):
        if not node:
            return
        # if R child
        if node.right:
            d[i] += node.right
        # if L child
        if node.left:
            d[i+1] += node.left

        dfs(node.right, d, i)
        dfs(node.left, d, i+1)
    # unsure if I should put d = dfs(root, d, 0)
    dfs(root, d, 0)

    # should be list of integer sums [7, 17, 14]
    return d.values()


# tried using q and sum array, order of q summing up diagonals in L direction, not R direction
def diagonal_sum():    
    """given binary tree, calculate diagonal sum"""
    i = 0
    def dfs(node, q, sum_, i):
        if not node:
            return
        # if R child
        sum_[i] += node.right
        # if L child
        q.append(node.left)

        dfs(node.right, q, sum_, i)
        dfs(node.left, q, sum_, i+1)
    # add node.right until node.right == None
    # add node.left to q
    dfs(root, [], [], 0)
    # pop from q and add all up until hit none, then start new entry in result array
    j = 0
    while q:
        next_l = q.pop()
        if next_l:
            sum_[j] += next_l
        j += 1


class TrieNode:
    def __init__(self):
        # staring from 0, diff with A 
        self.children = [None] * 26
        # each node has a boolean, changed to True after finish insert
        self.isEnd = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
		# insert each char in correct posititon and then move my curr
        current = self.root

        for char in word:
            print("INSERT char", char)
            if not current.children[ord(char) - ord('a')]:
                # make new node if node does not exist
                current.children[ord(char) - ord('a')] = TrieNode()
            # move my current to that charcter
            current = current.children[ord(char) - ord('a')]     
        
        current.isEnd = True # end insert True meaning the word is in tree
        # print("current after INSERT", current.children, current.isEnd)

	# Search for a char if not there then return False or if there move my curr
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for char in word:
            # print("SEARCH char", char)
            if not current.children[ord(char) - ord('a')]:
                return False # that character is not present in that children
            # moving along to child node
            current = current.children[ord(char) - ord('a')]
        # if the last node isEnd is true, then it has been inserted before    
        return current.isEnd 
        
	# Search for a prefix if not there then return False or if there move my curr till my prefix ends and return True
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            # if the char is not a child, then it's not in the trie
            if not current.children[ord(char) - ord('a')]:
                return False 
            current = current.children[ord(char) - ord('a')]
        
        num_children = [x for x in current.children if x]
 
        return len(num_children)


# Escape Room Keypads- supposed to use Trie, using sets here

def numKeypadSolutions(wordlist, keypads):
    """input of 2 string arrays, output int array with num of words for each keypad"""
    # initialize ans array that contains num of words for each keypad
    ans = [0] * len(keypads)
    
    # convert each word in wordlist to a set
    words = [set(word) for word in wordlist if len(set(word)) <= 7]
    
    # for each keypad, check if word is subset of keypad and if key in word
    for i, keypad in enumerate(keypads):
        key = keypad[0]
        for word in words:
            if key in word and word.issubset(set(keypad)):
                ans[i] += 1

    return ans


print(numKeypadSolutions(['APPLE', 'PLEAS', 'PLEASE', 'DOG'], ['PBNEDAL', 'OESADLP', 'MOTLAJF', 'GBLKORD']))