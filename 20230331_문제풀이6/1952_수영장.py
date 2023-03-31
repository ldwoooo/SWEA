def backtracking(i, n, cost):
    '''
    :param i: 시작 인덱스
    :param n: 끝
    :param cost: 누적 합
    '''
    global minV

    if i >= n:                          # 끝에 도달하면 최소값 비교
        minV = min(minV, cost)
        return
    
    if minV < cost:                     # 최솟값보다 크면 굳이 더하지마
        return
    
    backtracking(i + 1, n, cost+plan[i]*d)      # 하나씩 끝까지 이동하면서 일일 수강료로 계산
    backtracking(i + 1, n, cost+m1)             # 하나씩 백트래킹으로 되돌아오면서 한달 수강료로 계산
    # 다음과 같이 줄일 수 있다.
    # backtracking(i + 1, n, cost + min(plan[i]*d, m1))
    backtracking(i + 3, n, cost+m3)             # 되돌아오면서 세달 수강료로 계산


T = int(input())

for tc in range(1, T + 1):
    d, m1, m3, y = map(int, input().split())
    plan = list(map(int, input().split()))
    minV = y
    backtracking(0, 12, 0)
    print(f'#{tc}', minV)
