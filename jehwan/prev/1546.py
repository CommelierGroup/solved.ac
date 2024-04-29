n = int(input())
s = list(map(int, input().split()))

m = max(s)

print(sum(map(lambda x: x / m * 100, s)) / n)
