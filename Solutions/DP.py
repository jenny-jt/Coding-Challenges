# 3 1 8 2 5 -> 1 2 5
# import doctests

# L[3] = 2 
# L[0] = 1
# L[2] = 1 + Max(L[0], L[1])
# L[4] = 1 + max{L[1], L[3], L[0]}

# 5 2 8 6 3 6 9 5 -> 

def find_inc(n):
    """ takes array of int n, returns length of longest increasing subsequence
    """
    dp = [1] * len(n)
    
    for idx in range(len(n)):
        # calculate subproblems 
        # l[i] = 1 + max(subproblems)
        subproblems = [dp[k] for k in range(idx) if n[k] < n[idx]]
        dp[idx] += max(subproblems, default=0)
    
    return max(dp, default=0)

print(find_inc([5 ,2 ,8, 6, 3, 6, 9, 5]))
