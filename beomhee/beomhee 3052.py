user_list = [0]*10
for i in range(10) :
    user_list[i] = int(input())
rest_list = [item%42 for item in user_list]
rest_count = [0]*42
for i in range(10) :
    rest_count[rest_list[i]] += 1
count = 0
for i in range(42) :
    if rest_count[i] != 0 :
        count += 1
print(count)