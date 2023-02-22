def inorder(i, N):
    # 중위순회
    if i <= N:                                          # i == N이 될 때까지
        inorder(i * 2, N)                               # 왼쪽 자식 순회
        tree.append(i)                                  # 왼쪽 순회하고 오른쪽으로 넘어갈 때 순회 순서 넣어줌
        inorder(i * 2 + 1, N)                           # 오른쪽 자식 순회


for tc in range(1, 11):
    N = int(input())
    info = [input().split() for _ in range(N)]
    tree = []                                           # 순회 순서를 넣어줄 tree
    inorder(1, N)

    for i in range(N):
        for j in range(N):
            if tree[i] == int(info[j][0]):              # 순회 순서가 정보에 있는 숫자와 같으면
                tree[i] = info[j][1]                    # 순서 순자를 문자로 바꿔줌

    # print(info)
    # print(tree)

    print(f'#{tc}', end = ' ')                          # 출력

    for k in range(N):
        print(tree[k], end = '')
    print()
