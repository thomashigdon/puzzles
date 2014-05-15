a = [ 1, 5, 10, 25, 50, 100]
def coins(N, k):
    if k < 0 or N < 0: return 0
    if N == 0: return 1
    return coins(N, k-1) + coins(N - a[k], k)

for i in range(101):
    print i, coins(i, 3)
