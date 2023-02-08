T = int(input())

for tc in range(1, T+1):
    arr = list(input())
    arr2 = list(input())

    counts = [0] * len(arr)
    for i in range(len(arr)):

        c = 0
        for j in arr2:
            if arr[i] == j:
                c += 1
                
        counts[i] = c
    print(f'#{tc}', max(counts))
