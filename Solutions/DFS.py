# Implement depth first search
# Input: A node n, value v
# Output: a boolean representing whether the node is in the tree
# Extra challenge: Efficiently print the path you took to find the node
def depth_first_search(graph, start, v):
    """
        given graph and starting node, return True if node with value v in graph, otherwise False
        >>> depth_first_search({0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}, 0, 2)
        True
    """

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


if __name__ == '__main__':
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED!")
    print()