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

#### 2. Subset Sum


# naive solution: quadratic run time
def subset_sum(nums, target):
    res = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                res.append([nums[i], nums[j]])
    if res:
        return (True, res[0])

    return False


print(subset_sum([3, 34 , 4 , 12 , 5 , 2] , 9))


# using hashmap .045 runtime
def subset_sum(nums, target):
    """given array of nums, return a subset that adds up to target"""

    nums.sort()
    d = {}

    for num in nums:
        other = target - num
        if num in d:
            return (d[num], num)
        else:
            d[other] = num


nums = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum(nums, target))


# using dp, lots of unnecessary work but .035sec runtime vs .045 runtime
def subset_sum(nums, target):
    """given array of nums, return a subset that adds up to target"""

    nums.sort()
    dp = [[] for i in range(target + 1)]

    for i in range(1, len(dp)):
        for num in nums:
            if i - num in nums:
                dp[i].append([num, i-num])

    return dp[target][0]


nums = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum(nums, target))