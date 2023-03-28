
def f(i, k):
    global minV
    if i == k:
        s = e[0][p[0]]              # 사무실 -> 첫 구역
        for j in range(1, k):
            s += e[p[j-1]][p[j]]
        s += e[p[k-1]][0]           # 마지막 구역 -> 사무실
        if minV > s:
            minV = s

    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = arr[j]
                f(i+1, k)
                used[j] = 0


T = int(input())

for tc in range(1, T+1 ):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]

    arr = [i for i in range(1, N)]  # 사무실 0번, 각 구역 1 ~ N - 1번
    p = [0] * (N-1)
    used = [0]*(N-1)
    minV = 10000
    f(0, N-1)
    print(f'#{tc}', minV)