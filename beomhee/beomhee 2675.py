T = int(input())
R = [0]*T
S = ['_']*T
for i in range(T) :
    second_line = input().split(' ')
    R[i] = int(second_line[0])
    S[i] = second_line[1]

for i in range(T) :
    for item in S[i] :
        for j in range(R[i]) :
            print(item, end='')
    print()


