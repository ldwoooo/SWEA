def inorder(i, N):
    # 중위순회
    if i <= N:
        inorder(i * 2, N)               # 왼쪽 자식 순회
        tree.append(i)                  # 왼쪽 자식 거치고 오른쪽 넘어 갈때 처리해줌
        inorder(i * 2 + 1, N)           # 오른쪽 자식 순회
    # else:
    #     return


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    tree = []                           # 탐색 순서를 넣어줄 tree
    inorder(1, N)

    a = b = 0
    for i in range(len(tree)):
        if tree[i] == 1:
            a = i + 1
        elif tree[i] == N // 2:
            b = i + 1

    print(f'#{tc}', a, b)

# ---------------------------------------------------------------------------
# 연주님 코드
# 탐색 순서를 넣어주는 거 대신 cnt를 세서 tree[i]번째에 넣어줌
def f(i, N):  # 중위순회
    global cnt
    if i <= N:
        f(i * 2, N)
        cnt += 1
        tree[i] = cnt
        f(i * 2 + 1, N)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    cnt = 0
    f(1, N)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')