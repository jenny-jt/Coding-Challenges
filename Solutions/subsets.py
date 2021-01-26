###### subset_sum
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
