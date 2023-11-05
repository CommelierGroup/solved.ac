user_input = input()
input_list = user_input.split()
int_list = [int(item) for item in input_list]
if (int_list[0] >= -10000) & (int_list[1] <= 10000) :
    if int_list[0] > int_list[1] :
        print(">")
    elif int_list[0] < int_list[1] :
        print("<")
    else :
        print("==")