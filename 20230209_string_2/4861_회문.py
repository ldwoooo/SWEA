# 회문 찾는 함수
def palindrome(arr):

    i = 0
    j = 0
    k = M - 1
    if N == M:

        while i < N and j < M // 2:         # j가 회문 길이의 반까지만 가도 충분

            if arr[i][j] == arr[i][k]:
                j += 1
                k -= 1

            else:
                i += 1
                '''
                초기화 부분이 틀렸었음
                반례 : 회문 앞부분에 맞는 부분이 있으면 탐색구간이 달라진다
                
                      ex) UJAJQVSYYU
                          JAEZNNZEAJ
                          -> U 와 U가 같아서 j+1, k-1로 탐색 구간이 달라지는데
                             else 에서 초기화를 안해줘서 JAEZNNZEAM인 경우에도 출력이 되는 반례 생김
                '''
                j = 0
                k = M - 1

        if j == M // 2:
            return arr[i]
        else:
            return change(arr)
    else:

        count = 0
        while i < N and k > 0:                  # 회문을 찾으면 k의 값은 0 또는 -1이 됨

            if arr[i][j] == arr[i][j + k]:      # i열 j번째 와 i열 j + (M-1)이 같으면
                j += 1                          # j도 1씩 커지기 때문에 인덱스가 -1 되려면 k는 -2
                k -= 2

                count += 1
                '''
                else 이후, j 초기화 부분이 틀렸음
                반례 : 회문이 있는 구간 앞 부분에서 조건문을 만족하는 부분이 있으면
                      j가 카운팅 되면서 탐색 하다가 같지 않은 문자를 만나 else 로 빠지면
                      j가 그 이후 문자부터 탐색하게 되어서 반례가 발생
                      
                      ex)NZEPLJAEZNNZEAJ 
                         -> NZE~~EZN 이 같아서 탐색하다 P 와 A가 달라서 else 로 빠지게 되는데
                            이후 j가 Z부터가 아닌 P부터 탐색을 시작해서 반례가 발생
                      
                해결 : 탐색하면서 count 를 해주고 틀려서 else 로 빠졌을 때,
                      다시 j 다음 문자부터 탐색할 수 있게 해줌 
                '''

            else:                               # 회문이 아니면
                j = j - count + 1               # j 증가 및 k 초기화
                k = M - 1
                count = 0

                if j > N - M:                   # j가 회문 길이를 뺀 행의 길이를 초과하면
                    i += 1
                    j = 0

        if k <= 0:
            return arr[i][j-(M//2): j-(M//2) + M]   # 회문을 찾으면 j는 회문 길이의 절반만큼이 됨
        else:
            return change(arr)


# 전치행렬로 바꿔주는 함수
def change(arr):
    # '0'으로 채워진 NxN 생성
    na = [['0'] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            na[i][j] = arr[j][i]
    # 바뀐 행렬 다시 회문 함수로 반환
    return palindrome(na)


# 입력 받는 구간
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr2 = [list(map(str, input())) for _ in range(N)]

    # 출력 구간
    print(f'#{tc}', end=' ')
    for x in palindrome(arr2):
        print(x, end='')
    print()

