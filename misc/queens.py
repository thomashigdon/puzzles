def takable(p1, p2):
    return p1[0] == p2[0] or \
           p1[1] == p2[1] or \
           abs(p2[1] - p1[1]) == abs(p2[0] - p1[0])

blah = set()
def queens(pairsleft, qs):
    if len(qs) == 8:
        return qs
    for p in pairsleft:
        newpairs = []
        for q in pairsleft:
            if p == q: continue
            if not takable(p, q):
                newpairs.append(q)
        if not frozenset(qs + [p]) in blah:
            res = queens(newpairs, qs + [p])
            if res:
                blah.add(frozenset(qs + [p]))
                print res

allpairs = [ (x,y) for x in range(8) for y in range(8) ]
queens(allpairs, [])
print blah
