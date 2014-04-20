def isPerm1(A, B):
    return list(sorted(A)) == list(sorted(B))

from collections import Counter
def isPerm2(A, B):
    return list(Counter(A).elements()) == \
            list(Counter(B).elements())

def isPerm3(A, B):
    hists = [ {}, {} ]
    for i, item in enumerate([ A, B]):
        for thing in item:
            if thing not in hists[i]:
                hists[i][thing] = 1
            else:
                hists[i][thing] += 1
    return hists[0] == hists[1]

yesA = "abcd"; yesB = "dcba"
noA = "abc"; noB = "abd"

print isPerm1(yesA, yesB), isPerm1(noA, noB)
print isPerm2(yesA, yesB), isPerm2(noA, noB)
print isPerm3(yesA, yesB), isPerm3(noA, noB)
