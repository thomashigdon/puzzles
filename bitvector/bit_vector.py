#!/usr/bin/python

import sys

class BitVector(object):
    def __init__(self, string, index):
        self.index = index
        self.vector = [int(x) for x in string]
        self.parent = None
        self.child = None

    def sum(self):
        """ Return the number of ones in a BitVector
        """
        return sum(self.vector)

    def __sub__(self, other):
        """ Computes the Hamming distance between two BitVectors
        """
        return sum([x != y for x,y in zip(self.vector,other.vector)])

lines = sys.stdin.readlines()

bit_vectors = [BitVector(line.strip(), index) for index, line in enumerate(lines)]

def my_cmp(x,y):
    return x[1] - y[1]

vector_dict = {}

for vector in bit_vectors:
    diffs = [(vector_temp, vector - vector_temp) for vector_temp in bit_vectors]
    #print diffs
    diffs.sort(cmp=my_cmp)
    print diffs[1][1], diffs[2][1], diffs[3][1], diffs[-1][1]#, float(sum(diffs))/len(diffs)
    vector.parent = diffs[1][0].index
    vector.child  = diffs[2][0].index
    vector_dict[vector.index] = vector
    print 'vector %d: parent: %d child: %d' % (vector.index, vector.parent,
                                               vector.child)


