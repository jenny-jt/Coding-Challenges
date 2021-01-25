# Strings
1. Non-repeating Character
Given a string, return the first non-repeating char in a string
Example 1: “cabc” -> a
Example 2: “abc” -> a
Example 2: “bacab” -> c

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

    class DLL:
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
            if curr.data == data:
                self.head = curr.next
                self.head.prev = None

            while curr.next: # not tail:
                if curr.data == data:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
            else: #curr.next = None so curr is the tail
                if curr.data == data:
                    curr.prev.next = None

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

