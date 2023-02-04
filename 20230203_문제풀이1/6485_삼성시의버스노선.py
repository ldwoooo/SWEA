T = int(input())

for tc in range(1, T + 1):
    # list comprehension을 이용해 조건에 따라 입력
    N = int(input())
    bus_range = [list(map(int, input().split())) for i in range(N)]
    P = int(input())
    C = [int(input()) for j in range(P)]

    # 미리 counts 리스트를 P만큼 0으로 채워 넣고 조건에 따라 1씩 더한다
    counts = [0] * P
    for y in range(len(bus_range)):

        for x in range(P):
            # 리스트 형태인 bus_range을 범위화
            if C[x] in range(bus_range[y][0], bus_range[y][1] + 1):
                counts[x] += 1

            else:
                counts[x] += 0

    print(f'#{tc}', *counts)
