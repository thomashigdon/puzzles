#!/usr/bin/python

import random
import sys

def main():
    if len(sys.argv) < 2:
        print 'ack you need to enter a number'
        sys.exit()
    num = int(sys.argv[1])

    originator = ""
    for i in range(num):
        originator += '1' if random.random() < 0.5 else '0'

    lines = [originator]

    for i in range(num - 1):
        line = ""
        for j in range(num):
            if random.random() < 0.20:
                line += str(1 - int(lines[i][j]))
            else:
                line += lines[i][j]
        lines.append(line)

    indices = range(len(lines))

    random.shuffle(indices)

    x = open('outfile', 'w')
    y = open('order', 'w')

    for index in indices:
        x.write(str(lines[index]) + '\n')
        y.write(str(index) + '\n')

if __name__ == "__main__":
    main()
