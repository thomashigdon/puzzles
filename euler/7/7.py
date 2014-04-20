import lib
N = 2400

num = 2
primes = []
while len(primes) < N:
    if lib.is_prime(num):
        primes.append(num)
    num += 1

print primes[-1]
