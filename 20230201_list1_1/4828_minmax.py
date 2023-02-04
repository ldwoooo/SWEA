T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
 
    N = int(input())
    arr = list(map(int, input().split()))
 
    maxV = arr[0]
    minV = arr[0]
 
    for i in range(N):
        if maxV < arr[i]:
            maxV = arr[i]
        if minV > arr[i]:
            minV = arr[i]
    print(f'#{test_case} {maxV-minV}')