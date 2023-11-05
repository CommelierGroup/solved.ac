T = int(input())
H = [0]*T #층수
W = [0]*T #각층의 방 수 
N = [0]*T #몇 번쨰 손님

for i in range(T) :
    H[i], W[i], N[i] = input().split()
    H[i] = int(H[i])
    W[i] = int(W[i])
    N[i] = int(N[i])

for i in range(T) :
    num_div = int((N[i] -1)/ H[i])
    num_rest = N[i] % H[i] 
    num_front = 0
    num_back = 0
    if num_rest == 0 :
        num_front = H[i]
    else :
        num_front = num_rest
    num_back = num_div + 1
    if num_back < 10 :
        print(str(num_front)+"0"+str(num_back))
    else :
        print(str(num_front)+str(num_back))

        