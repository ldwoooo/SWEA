T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    Ci = list(map(int, input().split()))

    # 오름차순 정렬
    Ci.sort()

    minV = 1000
    for i in range(N - 2):                          # 소 박스
        for j in range(i + 1, N - 1):               # 중 박스
            if Ci[i] != Ci[i + 1] and Ci[j] != Ci[j + 1]:   # 같은 크기가 다른 박스에 들어가는 경우 제외
                A = i + 1
                B = j - i
                C = N - 1 - j
                if A * B * C != 0 and A <= N // 2 and B <= N // 2 and C <= N // 2:  # 빈 박스 없고 절반 초과하는 박스가 없으면
                    if minV > max(A, B, C) - min(A, B, C):
                        minV = max(A, B, C) - min(A, B, C)
    if minV == 1000:
        minV = -1
    print(f'#{tc}', minV)