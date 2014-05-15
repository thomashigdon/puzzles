count = 0
m = {}
def insub(A):
    if tuple(A) in m: return m[tuple(A)]
    global count
    count += 1
    if len(A) == 1: return A
    maxheight = 1
    maxstack = []
    for i, a in enumerate(A):
        result = A[:i] + A[i+1:]
        stack = insub(result)
        if stack and a[0] < stack[0][0] and a[1] < stack[0][1]:
            stack = [ a ] + stack
        if len(stack) > maxheight:
            maxheight = max(len(stack), maxheight)
            maxstack = stack
    m[tuple(A)] = maxstack
    return maxstack

A = [ (90,100), (70,150), (56,90), (75,190), (60,95), (68,110) ]
print insub(sorted(A))
print count
