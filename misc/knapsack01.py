
# si, vi
p1 = [ (3,5), (1,2), (5,6) ]
p2 = [ (1,1), (4,10), (1,2) ]

# M(i, j) = optimal knapsack value of the first i items for a j-size knapsack
# M(1, 1) = optimal knapsack value of the first item of a size 1 knapsack
# M(i, j) = max { M(i - 1, j),  M(i - 1, j - si) + vi }

def knapsack01(items, C):
    M = [ ]
    for i, item in enumerate(items):
        M.append( [ item[1] ] )
        for j in xrange(0, C):
            if item[1] > M[i][j]:
                M[i]
            rmax = M[i]
            M[i].append(

print knapsack(p1, 10)
print knapsack(p1, 5)
print knapsack(p2, 10)
