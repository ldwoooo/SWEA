def inorder(n):
    # 전위순회
    global count
    if n == 0:
        return
    count += 1
    inorder(left[n])                                    # 왼쪽 자식 순회
    inorder(right[n])                                   # 오른쪽 자식 순회


T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    node = list(map(int, input().split()))

    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for i in range(E):                                  # 부모 노드를 인덱스로 나타냄
        if left[node[i * 2]] == 0:
            left[node[i * 2]] = node[i * 2 + 1]
        else:
            right[node[i * 2]] = node[i * 2 + 1]
    # print(left)
    # print(right)

    count = 0
    inorder(N)
    print(f'#{tc}', count)
