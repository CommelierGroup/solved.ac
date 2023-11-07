user_number = [0]*3
for i in range(3):
    user_number[i] = int(input())

A = user_number[0]
B = user_number[1]
C = user_number[2]

number_count = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
D = str(A*B*C)
for i in range(len(D)) :
    cha = D[i]
    number_count[cha] += 1

for i in range(10) :
    print(number_count[str(i)])