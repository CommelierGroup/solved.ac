T = int(input())
A = [0]*T
B = [0]*T
for i in range(T) :
    A[i], B[i] = input().split()
    A[i] = int(A[i])
    B[i] = int(B[i])
for i in range(T) :
    print(A[i]+B[i])
