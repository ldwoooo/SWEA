T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))

    maxidx = minidx= 0

    for i in range(N):
        if ai[maxidx] <= ai[i]:
            maxidx = i
        if ai[minidx] > ai[i]:
            minidx = i

    print(f'#{tc}', abs(maxidx - minidx))