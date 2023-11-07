words = [-1] * 26
for i, w in enumerate(input()):
    if words[ord(w) - 97] != -1:
        continue

    words[ord(w) - 97] = i

for w in words:
    print(w, end=' ')
