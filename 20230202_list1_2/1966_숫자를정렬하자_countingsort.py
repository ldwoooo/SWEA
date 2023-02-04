T = int(input())

for ts in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 입력받은 arr의 최댓값 구하는 과정
    maxV = 0
    for i in range(N):
        if maxV < arr[i]:
            maxV = arr[i]

    # 최댓값 만큼의 자리를 만든다
    counts = [0] * (maxV + 1)

    # arr에 들어있는 숫자 카운팅
    for x in arr:
        counts[x] += 1

    # 카운팅 된 숫자 누적
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    # 입력받은 arr 배열의 크기 만큼의 sort 만들어주고
    # arr 배열에 해당하는 숫자을 개수를 누적한 리스트에 매칭해서 정렬해줌
    sort = [0] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        counts[arr[i]] -= 1
        sort[counts[arr[i]]] = arr[i]

    print(f'#{ts}', *sort)

