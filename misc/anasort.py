from collections import defaultdict
def anasort(A):
    ordlist = [(sum(ord(l) for l in word), len(word), word) for word in A ]
    h = defaultdict(lambda: [])
    for o in ordlist:
        h[(o[0], o[1])].append(o[2])
    return sum([h[k] for k in h], [])

print anasort(["ab", "ba", "abc", "def", "fed", "cab", "bac", "fde"])
