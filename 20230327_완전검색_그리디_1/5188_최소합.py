T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_arr = [[0] * N for _ in range(N)]           # 누적합을 기록할 배열 생성
    sum_arr[0][0] = arr[0][0]                       # 첫번째 값은 그대로

    for i in range(N):
        for j in range(N):
            minV = 1000
            for di, dj in [[0, -1], [-1, 0]]:       # 델타로 2차배열 돌면서
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:     # 가능 인덱스에 있고 새로운 최소값 갱신
                    new = sum_arr[ni][nj]           # 누적합 배열의 왼쪽, 위에서 가져온 값
                    if minV > new:
                        minV = new
            if sum_arr[i][j] == 0:                  # 첫번째 값을 제외해주기 위해
                sum_arr[i][j] = arr[i][j] + minV    # 기존 배열에서 왼쪽, 위 값 중 작은 값 가져와

    # print(sum_arr)
    print(f'#{tc}', sum_arr[N - 1][N - 1])
# -------------------------------------------------------------------------------------------------
# 교수님 코드
def f(i, j, N, s):
    global minV
    if i >= N or j >= N:
        return
    elif i == N - 1 and j == N - 1:
        s += arr[i][j]
        if minV > s :
            minV = s
 
    else:
        f(i, j + 1, N, s + arr[i][j])
        f(i + 1, j, N, s + arr[i][j])
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 1000
    s = 0
    f(0, 0, N, s)
    print(f'#{test_case}', minV)
