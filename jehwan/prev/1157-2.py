# 68 ms

ords = input().upper()
counter = [0] * 26

for i, x in enumerate(range(65, 91)):
    counter[i] = ords.count(chr(x))

max_val = max(counter)
max_val_cnt = counter.count(max_val)

print('?' if max_val_cnt > 1 else chr(65 + counter.index(max_val)))
