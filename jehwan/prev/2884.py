h, m = map(int, (input().split()))

t_m = m - 45
t_h = h

if t_m < 0:
    t_m = 60 + t_m
    t_h = h - 1

if t_h < 0:
    t_h = 24 + t_h

print(t_h, t_m)
