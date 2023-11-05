user_list = [0]*9
for i in range(9) :
    user_list[i] = int(input())

max_number = 0
max_index = 0
for i in range(9) :
    if max_number < user_list[i] :
        max_number = user_list[i]
        max_index = i
    
print(max_number)
print(max_index+1)