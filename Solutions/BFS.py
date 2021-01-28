def BFS(graph, root, v):
    """given root of graph and value of v, return True if node with value v is in graph
        >>> BFS({0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}, 0, 2)
        True
    """

    visited = set()
    q = [root]

    if root == v:
        return True

    # if not v, then add it to visited
    visited.add(root)

    while q:
        curr = q.pop(0)
        visited.add(curr)

        if curr == v:
            return True

        # add adjacent nodes to q if not already visited
        for node in graph[curr]:
            if node not in visited:
                q.append(node)

    return False


if __name__ == '__main__':
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED!")
    print()