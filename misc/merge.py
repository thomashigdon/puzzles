def merge(A, Alen, B, Blen):
    finalpos = Alen + Blen - 1
    Alen -= 1
    Blen -= 1
    import pdb; pdb.set_trace()
    while Blen >= 0:
        if Alen >= 0 and A[Alen] > B[Blen]:
            A[finalpos] = A[Alen]
            Alen -= 1
        else:
            A[finalpos] = B[Blen]
            Blen -= 1
        finalpos -= 1
    return A

print merge([3,4, 0, 0], 2, [1,2], 2)
print merge([1,2, 0, 0], 2, [3,4], 2)
