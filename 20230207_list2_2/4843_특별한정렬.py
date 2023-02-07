T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    i = 0
    x = 1
    new_arr = []
    while True:

        if i == 10:
            print(f'#{tc}', *new_arr)
            break

        # 선택정렬을 활용해 최댓값 맨 앞으로 가져온다
        for j in range(x, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        new_arr.append(arr[i])

        i += 1
        x += 1
        # 최솟값을 그 다음 인덱스로 가져온다
        for k in range(x, len(arr)):
            if arr[i] > arr[k]:
                arr[i], arr[k] = arr[k], arr[i]
        new_arr.append(arr[i])

        i += 1
        x += 1