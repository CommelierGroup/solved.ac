n = int(input())

if n == 1:
    print(666)
    exit(0)

x = 1
i = 667

while True:
    c = 0
    for s in str(i):
        if s != '6':
            c = 0
        else:
            c += 1

        if c == 3:
            x += 1

    if x == n:
        print(i)
        exit(0)

    i += 1
