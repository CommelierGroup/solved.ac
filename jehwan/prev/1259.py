while True:
    s = input()

    if s == '0':
        exit(0)

    print('yes' if s == s[::-1] else 'no')
