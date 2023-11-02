nums = list(enumerate(map(lambda _: int(input()), range(9))))

m = max(nums, key=lambda x: x[1])

print(m[1])
print(m[0] + 1)
