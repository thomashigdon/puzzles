import sys
def sortstack(s):
    s2 = []
    if len(s) == 0: return
    limit = -1
    while s[-1] != limit:
        minitem = s[-1]
        minitemcount = 0
        while not len(s) == 0 and s[-1] > limit:
            it = s.pop()
            if it < minitem:
                minitemcount = 1
                minitem = it
            elif it == minitem:
                minitemcount += 1
            s2.append(it)
        for i in range(minitemcount): s.append(minitem)
        while not len(s2) == 0:
            it = s2.pop()
            if it == minitem:
                continue
            s.append(it)
        limit = minitem

s = [ 5, 5, 1 , 2, 0, 10 , 0, 4]
sortstack(s)
print s
