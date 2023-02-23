def enq(n):
    global last
    for i in range(N):
        last += 1
        c = last                                                # 자식 노드
        p = last // 2                                           # 부모 노드

        heap[c] = node[i]                                       # heap에 입력받은 node를 순차적으로 넣어줌
        while c != 1:                                           # 자식이 루트에 올라올 때까지 반복
            if heap[c] < heap[p]:                               # 부모가 자식보다 크면 바꿔줘
                heap[c], heap[p] = heap[p], heap[c]
                c = p                                           # 옮긴 노드 번호로 수정
                p //= 2                                         # 2로 나눠주며 조상 노드로 변경
            else:
                break

    ans = 0
    while n != 1:                                   # 입력받은 노드 번호가 루트에 올라올 때까지 반복
        ans += heap[n // 2]                         # 부모부터 조상까지 다 더해
        n //= 2

    return ans


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    node = list(map(int, input().split()))

    heap = [0] * (N + 1)                            # 힙과 마지막 노드 생성
    last = 0

    print(f'#{tc}', enq(N))