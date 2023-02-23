def enq(i):

    if tree[i] not in op:
        return tree[i]
    else:
        r1 = enq(left[i])
        r2 = enq(right[i])

        if tree[i] == '+':
            tree[i] = r1 + r2
        elif tree[i] == '-':
            tree[i] = r1 - r2
        elif tree[i] == '*':
            tree[i] = r1 * r2
        elif tree[i] == '/':
            tree[i] = r1 // r2

        return tree[i]


for tc in range(1, 11):
    N = int(input())

    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    op = ['+', '-', '*', '/']

    for _ in range(N):
        info = input().split()
        node = int(info[0])

        if len(info) == 4:
            tree[node] = info[1]
            left[node] = int(info[2])
            right[node] = int(info[3])
        else:
            tree[node] = int(info[1])

    print(f'#{tc}', enq(1))
