def func(i, j):
    if i == j:
        return i
    else:
        m = (i + j) // 2
        r1 = func(i, m)
        r2 = func(m + 1, j)
        return rsp(r1, r2)


def rsp(a, b):
    x = nums[a - 1]
    y = nums[b - 1]

    if x == 1 and y == 3:
        return a

    elif x == 3 and y == 1:
        return b

    else:
        if x > y:
            return a
        elif x < y:
            return b
        else:
            return a


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    print(f'#{tc}', func(1, N))

