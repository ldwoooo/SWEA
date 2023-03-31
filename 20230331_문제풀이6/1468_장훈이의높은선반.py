
# 비트연산자
T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    minV = sum(H)

    for i in range(1 << N):     # 부분집합의 수.2의 N승 개
        ans = 0
        for j in range(N):
            if i & (1 << j):    # AND 연산자. i를 2진수로 바꿔서 자리 값 비교해줌. 둘 다 1이면 1을 반환
                ans += H[j]     # 부분 집합의 합
        if ans >= B:            # 집합의 합이 선반보다 크고
            if minV > ans:      # 그 중 최소값을 구하기
                minV = ans
    print(f'#{tc}', minV - B)
# -------------------------------------------------------------
# 재귀
def f(i, j, ans):
    global minV

    if i == j:
        if ans >= B:
            if minV > ans:
                minV = ans
        # print(bit)
        return

    else:
        # bit[i] = 0
        f(i + 1, j, ans)
        # bit[i] = 1
        ans += H[i]
        f(i + 1, j, ans)


T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    # bit = [0] * N
    minV = sum(H)
    f(0, N, 0)
    print(f'#{tc}', minV - B)
