def is_prime(num):
    return set(prime_factors(num)) == set([num])

def prime_factors(N):
    inter_num = N
    factors = []
    while inter_num >= 2:
        for i in range(2,N+1):
            if inter_num % i == 0:
                factors.append(i)
                inter_num /= i
                break
    return factors
