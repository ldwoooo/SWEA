def postorder(i, N):
    # 후위 순회
    if tree[i] == 0:                                        # 리프를 만날 때 까지 순회하라
        if i <= N:
            postorder(i * 2, N)
            postorder(i * 2 + 1, N)
            tree[i] = tree[i * 2] + tree[i * 2 + 1]
    else:
        return

    return tree[L]                                          # L번째 값 반환

''' 혜진님 후위 순회 함수
def post_order(i, N):
    if i <= N:
        if arr[i] == 0:
            r1 = post_order(i*2, N)     # 왼쪽자식의 값 확인
            r2 = post_order(i*2+1, N)   # 오른쪽 자식 값 확인
            arr[i] = r1 + r2    # post_order(i*2) + post_order(i*2+1)
        return arr[i]
    else:
        return 0
'''

T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    tree = [0] * 10000

    for _ in range(M):                                      # 리프의 정보를 입력 받아서 트리 생성
        node, num = map(int, input().split())
        tree[node] = num

    print(f'#{tc}', postorder(1, N))
