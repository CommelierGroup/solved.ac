n, x = map(int, input().split())

for v in filter(lambda a: a < x, map(int, input().split())):
    print(v, end=' ')
