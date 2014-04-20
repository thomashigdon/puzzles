def findcompsize(A):
    last = A[0]
    count = 0
    strlen = 0
    for a in A:
        if last == a:
            count += 1
        else:
            strlen += (1 + len(str(count)))
            last = a
            count = 1
    return strlen

def comp(A):
    if not A: return
    last = A[0]
    out = []
    rc = 0
    for a in A:
        if a == last:
            rc += 1
        else:
            out.append(last + str(rc))
            rc = 1
            last = a
    out.append(last + str(rc))
    if len(out) > len(A): return A
    return out

print comp("aaaabbcccccd")
