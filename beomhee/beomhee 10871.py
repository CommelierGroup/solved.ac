N, X = input().split()
N = int(N)
X = int(X)
C = [0]*X
C = [int(item) for item in input().split()]
D = []
for item in C :
    if item < X :
        D.append(item)

for item in D :
    if D.index(item) != len(D) -1 :
        print(item, end=" ")
    else :
        print(item)