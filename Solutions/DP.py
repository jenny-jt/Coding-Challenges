#  3 1 8 2 5 -> 1 2 5
#  import doctests

#  L[3] = 2 
#  L[0] = 1
#  L[2] = 1 + Max(L[0], L[1])
#  L[4] = 1 + max{L[1], L[3], L[0]}

#  5 2 8 6 3 6 9 5 -> 

def find_inc(n):
    """ takes array of int n, returns length of longest increasing subsequence"""
    dp = [1] * len(n)
    print("n", n)

    for i in range(len(n)):
        print("i", i)
        subproblem = [dp[j] for j in range(i) if n[j] < n[i]]
        print(subproblem)
        dp[i] += max(subproblem, default=0)
        print("dp of i", dp[i])

    return max(dp, default=0)


print(find_inc([5, 2, 8, 6, 3, 6, 9, 5]))
