# 116 ms

from collections import Counter

groupBy = Counter(input().upper()).most_common()

if len(groupBy) == 1:
    print(groupBy[0][0])
else:
    print('?' if groupBy[0][1] == groupBy[1][1] else groupBy[0][0])
