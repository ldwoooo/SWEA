T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    profit = 0
    maxV = nums[N - 1]
    for i in range(N - 2, -1, -1):

        if nums[i] < maxV:
            profit += maxV - nums[i]

        maxV = max(maxV, nums[i])

    print(f'#{tc}', profit)
