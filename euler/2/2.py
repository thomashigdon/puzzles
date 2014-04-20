def fib(N):
    fibo = [ 1, 2 ]
    result = [ 2 ]
    while fibo[-1] < N:
        fibo.append(fibo[-2]+fibo[-1])
        if fibo[-1] % 2 == 0:
            result.append(fibo[-1])
    return result

print sum(fib(4e6))

