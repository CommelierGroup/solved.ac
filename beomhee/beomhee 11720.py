N = int(input())
T = [0]*N
st = input()
for i in range(N) :
    T[i] += int(st[i])
print(sum(T))