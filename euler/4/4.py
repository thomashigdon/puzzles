prod = 0

def is_palindrome(num):
    array = []
    div = 10
    while num > 0:
        array = [num % div] + array
        num = (num - (num % div)) / div

    front = 0
    back = len(array) - 1
    while array[front] == array[back]:
        if front == back or front == back - 1:
            return True
        front += 1
        back -= 1

    return False



for i in xrange(100,999):
    for j in xrange(100,999):
        if is_palindrome(i*j) and i*j > prod:
            prod = i*j

print prod


