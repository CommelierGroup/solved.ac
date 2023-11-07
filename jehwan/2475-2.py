# 모듈로 분배 법칙에 따라 미리 10 으로 나눈 뒤 더함

print(sum(int(x) ** 2 % 10 for x in input().split()) % 10)
