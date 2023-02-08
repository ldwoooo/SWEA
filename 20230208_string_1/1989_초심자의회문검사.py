T = int(input())

for tc in range(1, T + 1):
    word = input()
    nw = word[::-1]

    if word == nw:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)
