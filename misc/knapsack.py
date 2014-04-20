#!/usr/bin/python

# si, vi
p1 = [ (3,5), (1,2), (5,6) ]
p2 = [ (1,1), (4,10), (1,2) ]

# M(i) largest value for i items
# M = max { M(i - 1), max (M(i - sj) + vj) }
# M(1) =  max { M(0), max (M(1 - sj) + vj) }

def knapsack(items, ksize):
    M = [ (0,0) ]
    for k in xrange(1, ksize + 1):
        rmax = 0
        prev = 0
        for item in items:
            if item[0] > k: continue
            if M[k - item[0]][0] + item[1] > rmax:
                prev = item
                rmax = M[k - item[0]][0] + item[1]
        if M[-1][0] > rmax:
            M.append(M[-1])
        else:
            M.append((rmax, prev))
    return M[-1]

print knapsack(p1, 10)
print knapsack(p1, 5)
print knapsack(p2, 10)
