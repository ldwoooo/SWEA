T = int(input())
 
for tc in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    M_nums = list(map(int, input().split()))
 
    counts = [0] * 100
 
    for x in M_nums:
        counts[x] += 1
 
    i = 0
    cnt = 0
 
    while True:
        # 정류장에서 +K 했을 때 도착지점 이상이면 반복문 종료
        if i + K >= N:
            print(f'#{tc}', cnt)
            break
        # 정류장에서 +K 했을 때 값이 있으면, 이동 및 카운팅
        elif counts[i + K]:
            i += K
            cnt += 1
         
        else:
            # K-1 씩 이동하면서 값이 있는지 확인
            for j in range(K-1, -1, -1):
 
                if counts[i + j]:
                    i += j
                    cnt += 1
                    break
            # 정류장이 없으면 0 출력
            if j == 0:
                cnt = 0
                print(f'#{tc}', cnt)
                break