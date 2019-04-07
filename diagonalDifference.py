def diagonalDifference(arr,n):
    diag_1 = 0
    diag_2 = 0
    for i in range(n):
        diag_1 += arr[i][i]
        diag_2 += arr[i][n-i-1]
    return abs((diag_1)-(diag_2))

if __name__ == "__main__":
    arr = [[11,2,4],[4,5,6],[10,8,-12]]
    n = 3 # Value size array 3X3
    print(diagonalDifference(arr,n))

        