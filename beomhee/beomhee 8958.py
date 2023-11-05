T = int(input())
user_input = ["_"]*T

def scoring(answer) :
    count = 0
    score = 0
    for i in range(len(answer)) :
        if answer[i] == "O" :
            count += 1
            score += count
        else :
            count = 0
    return score

for i in range(T) :
    user_input[i] = input()
for item in user_input :
    print(scoring(item))