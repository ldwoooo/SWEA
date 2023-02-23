def inorder(i, N):
    if i <= N:
        inorder(i * 2, N)
        arr.append(tree[i])
        inorder(i * 2 + 1, N)


for tc in range(1, 3):
    N = int(input())

    tree = [0] * (N + 1)
    for _ in range(N):
        info = input().split()

        node = int(info[0])
        math = info[1]

        for _ in range(N + 1):
            tree[node] = math
    arr = []
    inorder(1, N)

    for i in range(N):
        if i == ''():

    print(arr)