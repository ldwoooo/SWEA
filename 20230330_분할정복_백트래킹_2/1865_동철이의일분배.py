def backtracking(i, n, ans):
    '''
    :param i: 행. 직원들
    :param n: 끝 인덱스. 직원 수
    :param ans: 누적 확률. 
    '''
    global maxV

    if i == n:                      # 끝에 도달하면 최대 성공 확률 비교
        maxV = max(maxV, ans)
        return

    if maxV > ans:                  # 이미 확률이 적으면 비교할 필요 없음
        return

    for j in range(N):
        if per[i][j]:               # 확률이 0이면 볼 필요도 없다
            if visited[j] == 0:     # 방문하지 않았으면 방문하고
                visited[j] = 1
                backtracking(i + 1, n, ans * (per[i][j] * 0.01))    # 행 바꿔주고 확율을 누적해서 구해준다
                visited[j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    per = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    visited = [0] * N                               # 방문배열
    backtracking(0, N, 1)

    print(f'#{tc}', "{:.6f}".format(maxV * 100))    # 소수점 맞춰서 출력
