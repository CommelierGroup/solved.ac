n, m = map(int, input().split())

board = list(map(lambda _: input(), range(n)))

slide_n = n - 7
slide_m = m - 7

min_cnt = 999

for i in range(slide_n):
    for j in range(slide_m):
        cnt_start_b = 0
        cnt_start_w = 0

        for k in range(i, i + 8):
            for p in range(j, j + 8):
                if (k + p) & 1:
                    if board[k][p] != 'W':
                        cnt_start_b += 1
                    if board[k][p] != 'B':
                        cnt_start_w += 1
                else:
                    if board[k][p] != 'B':
                        cnt_start_b += 1
                    if board[k][p] != 'W':
                        cnt_start_w += 1

        min_cnt = min(min_cnt, cnt_start_b, cnt_start_w)

print(min_cnt)