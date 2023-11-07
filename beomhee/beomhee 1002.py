user_input = input()
input_list = user_input.split()
int_list = [int(item)for item in input_list]
C = int_list[0]/int_list[1]
print(C)