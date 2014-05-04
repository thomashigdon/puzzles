def parens(N):
    if N == 0: return set([""])
    if N == 1: return set(["()"])
    prev = parens(N - 1)
    result = set()
    for p in prev:
        for pos in range(len(prev) + 1):
            result.add(p[:pos] + "()" + p[pos:])
    return result

for i in range(5):
    print parens(i)
