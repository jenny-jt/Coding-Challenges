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
