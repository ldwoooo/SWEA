def backtraking(s, e, cnt):
    global minV
    if s == e:                      # 끝까지 이동
        minV = min(minV, cnt)       # 최소 충전값 갱신
        return
    if cnt >= minV:                 # 가지치기
        return                      # 최소 충전 값보다 더 충전하면 그 이후는 볼 필요 없음
    for i in range(charger[s], 0, -1):          # 가능성 체크
        if s + i <= e:                          # 멀리부터 갈 수 있으면
            backtraking(s + i, e, cnt + 1)      # 정류장으로 가봐


T = int(input())

for tc in range(1, T + 1):
    tmp = list(map(int, input().split()))

    N = tmp[0]
    charger = tmp[1:]
    minV = 100
    backtraking(0, N - 1, -1)
    print(f'#{tc}', minV)

