def row(arr):
    '''
    가로에 들어갈 수 있는 자리의 수 반환 함수
    '''
    ans = 0
    for i in range(N):              # 행렬을 하나씩 다 확인

        count = 0
        for j in range(N):

            if arr[i][j]:           # 1이면 카운팅
                count += 1
            else:                   # 0을 만나면 카운트가 K랑 같은지 확인하고 초기화
                if count == K:
                    ans += 1
                count = 0

        if count == K:              # 한 행을 다 돌았을 때 카운트가 K와 같은지 확인
            ans += 1

    return ans


def column(arr):
    '''
    세로에 들어갈 수 있는 자리의 수 반환 함수
    '''
    ans = 0
    for i in range(N):

        count = 0
        for j in range(N):

            if arr[j][i]:           # 가로 함수에서 행렬만 바꿔줌
                count += 1
            else:
                if count == K:
                    ans += 1
                count = 0

        if count == K:
            ans += 1

    return ans


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc}', row(arr) + column(arr))
