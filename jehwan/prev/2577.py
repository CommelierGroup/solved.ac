a, b, c = map(int, (input(), input(), input()))

stringify = str(a * b * c)

for x in range(10):
    print(stringify.count(str(x)))
