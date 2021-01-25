List of Problems for Interview Prep

# Strings
1. Non-repeating Character
Given a string, return the first non-repeating char in a string
Example 1: “cabc” -> a
Example 2: “abc” -> a
Example 2: “bacab” -> c

    # constant time solution: using hash map/set and DLL



# Arrays 
2: Subset Sum
Given array of numbers, return a subset that adds up to target value
Example 1: [3,34,4,12,5,2], 9
# {3, 34 , 4 , 12 , 5 , 2} sum=9 True 
# {2, 3, 4, 5, 12, 34}

# naive solution: quadratic run time
def subset_sum(nums, target):
    res = []
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                res.append([nums[i], nums[j]])
    if res:
        return (True, res[0])
    
    return False

print(subset_sum([3, 34 , 4 , 12 , 5 , 2] , 9))

# more optimized, dp
nums.sort()