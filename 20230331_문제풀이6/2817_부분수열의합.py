T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(1 << N):
        ans = 0
        for j in range(N):
            if i & (1 << j):
                ans += A[j]                 # 부분 집합의 합을 누적한다.
                if ans > K:                 # 이미 K를 넘어버리면 멈춰
                    break
        if ans == K:                    # 같으면 카운팅해
            cnt += 1

    print(f'#{tc}', cnt)