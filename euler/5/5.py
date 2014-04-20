import lib
import math

def nums_to_hist(nums):
    hist = {}
    for num in nums:
        if hist.has_key(num):
            hist[num] += 1
        else:
            hist[num] = 1
    return hist

factors = {}

N = 20

for x in range(2,N+1):
    nums = lib.prime_factors(x)
    hist = nums_to_hist(nums)
    for k,v in hist.iteritems():
        if factors.has_key(k):
            factors[k] = max(hist[k], factors[k])
        else:
            factors[k] = hist[k]

result = 1
print factors
for factor, times in factors.iteritems():
    result *= math.pow(factor, times)

print result
