def dfs(i, j, s):
    '''
    :param i: 현재 행
    :param j: 현재 열
    :param s: 현재 배열의 수
    '''

    if len(s) == 7:         # 수의 길이가 7이면
        ans.add(s)          # set 에 더해줘
        return

    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:   # 델타 탐색하면서
        ni, nj = i + di, j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:                 # 유효한 인덱스이면
            dfs(ni, nj, s + arr[ni][nj])                # 가봐


T = int(input())

for tc in range(1, T + 1):
    arr = [input().split() for _ in range(4)]   # 문자로 받아서 이어 붙이기
    ans = set()                         # set으로 바로 담아서 겹치는 수 자동 삭제
    for i in range(4):                  # 2차 배열을 탐색하면서 출발점 설정
        for j in range(4):
            dfs(i, j, arr[i][j])

    print(f'#{tc}', len(ans))
