import math
N = 100

sum_of_squares = sum([ math.pow(x, 2) for x in xrange(1, N+1) ])
square_of_sums = math.pow(sum(xrange(1, N+1)),2)

print square_of_sums
print sum_of_squares
print square_of_sums - sum_of_squares
