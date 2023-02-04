T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 공간으로 분리되어 있지 않으므로 str형태로 split 없이 리스트에 넣어줌
    num = list(map(int, input()))
    arr = []

    count = 0

    for i in num:
        if i == 0:
            count = 0
        # 누적합으로 각 인덱스에 각 카운트 값을 매칭
        if i:
            count += 1
        arr.append(count)
    # 카운트 값 중 최대 출력
    maxV = 0
    for j in range(N):
        if maxV < arr[j]:
            maxV = arr[j]

    print(f'#{tc}', maxV)