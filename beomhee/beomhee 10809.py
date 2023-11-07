S = input()
#a-z : 97-122 26개 0-25
alphabets = [-1]*26
for i in range(len(S)) :
    alphabets[ord(S[len(S)-i-1])-97] = len(S)-i-1

for i in range(len(alphabets)) :
    if i != 0 :
        print("",alphabets[i], end="")
    else :
        print(alphabets[i], end="")

