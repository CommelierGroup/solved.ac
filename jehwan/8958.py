from functools import reduce


def accumulate(acc, ch):
    if ch == 'X':
        acc[1] = 0
        return acc
    else:
        acc[1] += 1
        acc[0] += acc[1]
    return acc


n = int(input())

for _ in range(n):
    print(reduce(accumulate, input(), [0, 0])[0])
