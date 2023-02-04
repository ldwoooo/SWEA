T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
 
    maxV = 0
    minV = 1000000
 
    for i in range(N-M+1):  # M개의 이웃한 원소에서 가장 왼쪽
        s = 0               # i에서 시작하는 구간합
        for j in range(i, i + M):
            s += arr[j]
        # for j in range(M):
        #     s += arr[i+j]
 
        if maxV < s:
            maxV = s
 
        if minV > s:
            minV = s
 
    print(f'#{test_case} {maxV-minV}')