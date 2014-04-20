def rotate(A):
    N = len(A)
    for j in range(N/2):
        for i in range(j, N-j-1):
            print i, j, N-j
            #print i, j,  N - i - 1, N - j - 1
            print A[j][i], A[i][N-1-j], A[N-1-j][N-1-i], A[N-1-i][j]
            tmp = A[j][i]
            A[j][i] = A[N-1-i][j]
            tmp2 = A[i][N-1-j]
            A[i][N-1-j] = tmp
            tmp = A[N-1-j][N-1-i]
            A[N-1-j][N-1-i] = tmp2
            A[N-1-i][j] = tmp

    return A

import pprint
input1 = [ [1, 2], [3, 4] ]
input2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
input3 = [ [1, 2, 3, 4], [5, 6, 7, 8 ], [9, 10, 11, 12], [13, 14, 15, 16] ]
pprint.pprint(rotate(input1))
pprint.pprint(rotate(input2))
pprint.pprint(rotate(input3))
