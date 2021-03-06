# piecewise function

# deletion: lev(i-1, j) + 1   
# insertion: lev(i, j-1) + 1
# substitution: lev(i-1, j-1) + 1

# 2D array
def l_distance(a, b):
    m, n = len(a)+1, len(b)+1
    # initialize 2D matrix 1[0...m, 0..n] and set each el to 0
    ld = [[0]*(n) for i in range(m)]
    # print(ld)

    # set border values
    for i in range(m):
        ld[i][0] += i

    for j in range(n):
        ld[0][j] += j

    # fill in remaining values row, col
    for j in range(1, n):
        for i in range(1, m):
            # letters are same, take the value of the previous letters
            if a[i-1] == b[j-1]:
                # print("same", a[i-1], b[j-1])
                ld[i][j] += ld[i-1][j-1]
            else:
                # print("diff", a[i-1], b[j-1])
                # letters are diff, take the min of the 3 options (+/-/delta), and add 1
                ld[i][j] += min(ld[i-1][j], ld[i][j-1], ld[i-1][j-1]) + 1

    return ld[m-1][n-1]


print(l_distance("kitten", "sitting"))
