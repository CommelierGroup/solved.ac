user_input = input()
user_list = user_input.split()
user_int = [int(item) for item in user_list]

def check_ascending(user_int) :
    pre_item = 0
    for item in user_int :
        if item <= pre_item :
            return 0
        else :
            pre_item = item
    return 1

def check_descending(user_int) :
    pre_item = 9
    for item in user_int :
        if item >= pre_item :
            return 0
        else :
            pre_item = item
    return 1

if check_ascending(user_int) :
    print("ascending")
elif check_descending(user_int) :
    print("descending")
else :
    print("mixed")