for v in sorted(set(map(lambda _: input(), range(int(input())))), key=lambda x: (len(x), x)):
    print(v)
