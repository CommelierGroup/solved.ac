user_input = input()
input_list = [int(item) for item in user_input.split(" ")]
total_number = 0
for item in input_list :
    total_number += item*item
cert_number = total_number%10
print(cert_number)

