T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 10X10 배열에 0으로 초기화 시켜놈
    paper = [[0] * 10 for _ in range(10)]
    
    # 주어진 범위만큼 색칠한다
    for i in range(N):
        for j in range(arr[i][0], arr[i][2] + 1):
            for k in range(arr[i][1], arr[i][3] + 1):
                paper[j][k] += 1
    
    # 두 번 색칠되어 있는 갯수를 구함
    count = 0
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 2:
                count += 1
    print(f'#{tc}', count)