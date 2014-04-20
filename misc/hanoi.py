def hanoi(source, storage, target, num):
    print source, storage, target, num
    if num == 1:
        target.append(source.pop())
        assert len(target) == 1 or (target[-1] < target[-2])
        return
    hanoi(source, target, storage, num - 1)
    target.append(source.pop())
    hanoi(storage, source, target, num - 1)

def main():
    source = [ 10,9,8,7,6,5,4, 3, 2, 1 ]
    storage = []
    target = []
    hanoi(source, storage, target, len(source))
    print source, target, storage

if __name__ == '__main__':
    import sys
    sys.exit(main())
