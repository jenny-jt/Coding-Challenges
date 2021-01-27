#### 1. Non-repeating Character

# constant time solution: using hash map/set and DLL
def NonRepeatingChar(s):
    """
    Given a string s, return the first non-repeating char in s
    >>> NonRepeatingChar(“cabc”)
    a
    >>> NonRepeatingChar(“abc”)
    a
    >>> NonRepeatingChar(“bacab”)
    c
    """

    # implement DLL
    # add method; instantiate node and add it to DLL, adjust next and prev pointers
    # del method: find node, remove node, and reassign pointers
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    class DLL: # have a more descriptive name
        def __init__(self):
            self.head = None

        def add(self, data):
            new = Node(data)
            if not self.head:
                self.head = new
            else:
                curr = self.head
                while curr.next:
                    curr = curr.next
                curr.next = new
                new.prev = curr

        def remove(self, data):
            curr = self.head
            # if the head is the node that we want to remove
            if curr.data == data:
                self.head = curr.next
                self.head.prev = None
                return

            while curr.next: # not tail:
                curr = curr.next
                if curr.data == data:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    return
            else: # curr.next = None so curr is the tail
                if curr.data == data:
                    curr.prev.next = None
                    return

    seen = set()
    DLL = DLL()

    for char in s:
        if char not in seen:
            seen.add(char)
            DLL.add(char)
        else:
            DLL.remove(char)

    # if there are non-repeating chars
    if DLL:
        return DLL.head.data


print(NonRepeatingChar("cabc"))
print(NonRepeatingChar("bacab"))
