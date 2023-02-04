T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))

    count = 1
    counts = []
    for i in range(N - 1):
        # 기존의 값 + 1이 다음값과 같으면 count++
        if carrot[i] + 1 == carrot[i + 1]:
            count += 1
        else:
            count = 1
        counts.append(count)

    maxV = 0
    for j in range(len(counts)):
        if maxV < counts[j]:
            maxV = counts[j]

    print(f'#{tc}', maxV)
