n = int(input())

for i in range(n):
    h, w, g = map(int, input().split())

    room = g // h + 1
    floor = g % h

    if floor == 0:
        floor = h
        room -= 1

    print(f'{floor}{str(room).zfill(2)}')
