# Implement depth first search
# Input: A node n, value v
# Output: a boolean representing whether the node is in the tree
# Extra challenge: Efficiently print the path you took to find the node
def depth_first_search(graph, start, v):
    visited = set()
    stack = [start]

    while stack:
        curr = stack.pop()
        if curr == v:
            return True

        for node in graph[curr]:
            if node not in visited:
                stack.append(node)

    return False
