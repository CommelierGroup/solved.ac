prev = -1
counter = [7, 7]

for x in map(int, input().split()):
    if x == prev + 1:
        counter[0] -= 1
    elif x == prev - 1:
        counter[1] -= 1
    prev = x

if counter[0] == 0:
    print('ascending')
elif counter[1] == 0:
    print('descending')
else:
    print('mixed')
