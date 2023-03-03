T = int(input())

for tc in range(1, T + 1):                              # 입력
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    boong = [0] * 11112                                 # 도착하는 시간(초)의 최댓값 11,111
    time = [0] * 11112
    check = [0] * 11112

    for i in arr:                                       # 각 초에 몇명이 도착하는지 카운팅
        time[i] += 1
    for j in range(M, 11112, M):                        # 시간에 따라 붕어빵 굽기
        boong[j] += K

    # print(boong)
    for k in range(11111):                              # 인덱스로 돌기

        boong[k + 1] += boong[k] - time[k]              # 지금 있는 붕어빵 = 새로 만든 붕어빵 + 만들어논 붕어빵 - 팔린 붕어빵
        if boong[k] < time[k]:                          # 지금 있는 붕어빵보다 사람이 많으면 불가능
            print(f'#{tc}', 'Impossible')
            break
    else:                                               # 그렇지 않으면 가능
        print(f'#{tc}', 'Possible')


    # print(time)
    print(boong)
    
# ----------------------------------------------------------------------------------------------------------------
# 출력값 비교하기 위한 데이터 비교 코드
# A = [list(input().split()) for _ in range(1000)]
# B = [list(input().split()) for _ in range(1000)]
#
# for i in range(1000):
#     if A[i][1] != B[i][1]:
#         print(i)
