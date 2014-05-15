def howmany(N):
    if not N:
        return 0
    if N == 1:
        return 1
    if N == 2:
        return 2
    return howmany(N-3) + 4

def howmany2(N):
    if N < 0:
        return 0
    if N == 0:
        return 1
    return howmany2(N-1) + howmany2(N-2) + howmany2(N-3)

print [ howmany(x) for x in range(10) ]
print [ howmany2(x) for x in range(10) ]
