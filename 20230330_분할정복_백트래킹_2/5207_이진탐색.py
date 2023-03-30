def func(a, b):         # 이진 검색 함수
    '''
    이진 검색 함수.
    중간 값을 기준으로 찾는 값이 크면 오른쪽을 탐색
    찾는 값이 작으면 왼쪽을 탐색을 반복하며 중간 값과 같아질때(찾는 값이 있을 떄)까지 반복
    '''
    global cnt

    for i in b:         # b 배열에 있는 숫자 꺼내서 a에 있으면 검색 시작
        if i in a:
            check = 0               # 어느쪽으로 이동했는지 확인하기 위한 변수
            l = 0
            r = len(a) - 1
            # 값이 없어서 왼쪽 인덱스가 오른쪽 인덱스를 넘어갈 때까지
            # 사실 i가 a에 있는지를 검사했으므로 찾는 숫자가 a 안에 없을 수가 없으며 while True: 라 써도 무방함
            while l <= r:
                m = (l + r) // 2
                if i == a[m]:                       # 찾는 수가 중간값과 같으면 카운트
                    cnt += 1
                    break
                elif i > a[m] and check != 1:       # 중간 값보다 크고 오른쪽에 갔다 오지 않았으면
                    l = m + 1
                    check = 1                       # 오른쪽 탐색
                elif i < a[m] and check != 2:       # 중간 값보다 작고 왼쪽에 갔다 오지 않았으면
                    r = m - 1
                    check = 2                       # 왼쪽 탐색
                else:                               # 그렇지 않으면, 양쪽 구간을 번갈아 선택하지 않은 경우 멈춰!!
                    break


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_arr = list(map(int, input().split()))
    M_arr = list(map(int, input().split()))
    cnt = 0
    N_arr.sort()
    func(N_arr, M_arr)
    print(f'#{tc}', cnt)
