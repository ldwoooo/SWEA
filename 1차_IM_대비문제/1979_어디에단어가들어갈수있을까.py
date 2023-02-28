T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if puzzle[i][j]:
                count += 1
            else:
                if count == K:
                    ans += 1
                count = 0
        if count == K:
            ans += 1

    count = 0
    for j in range(N):
        count = 0
        for i in range(N):
            if puzzle[i][j]:
                count += 1
            else:
                if count == K:
                    ans += 1
                count = 0

        if count == K:
            ans += 1

    print(f'#{tc}', ans)