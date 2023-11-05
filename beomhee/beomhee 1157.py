user_input = input()
my_list = [0 for item in range(32)]

def insert_alphabet(alphabet) :
    if ord(alphabet) == 32 :
        return
    ascii_code = 0
    if ord(alphabet) > 96 :
        ascii_code = ord(alphabet)-32
    else :
        ascii_code = ord(alphabet)
    my_list[ascii_code-65] += 1
    return

for char in user_input :
    insert_alphabet(char)

max_count = 0
max_items = 0
max_index = 0
for i in range(32) :
    if max_count < my_list[i] :
        max_count = my_list[i]
        max_index = i
for i in range(32) :
    if max_count == my_list[i] :
        max_items += 1
if max_items > 1 :
    print("?")
else :
    print(chr(max_index + 65))