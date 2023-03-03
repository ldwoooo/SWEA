T = int(input())

for tc in range(1, T + 1):
    txt = [input() for _ in range(5)]
    # print(txt)
    ans = ''
    # # print(len(txt), txt[0][0])
    for j in range(15):
        for i in range(5):
            if j >= len(txt[i]):
                continue
            ans += txt[i][j]
    print(f'#{tc}', ans)
