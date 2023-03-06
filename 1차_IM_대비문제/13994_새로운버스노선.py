T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    bus = [0] * 1001

    for _ in range(N):
        tp, A, B = map(int, input().split())

        if tp == 1:                             # 일반 버스 일 때
            for i in range(A, B + 1):
                bus[i] += 1
        elif tp == 2:                           # 급행 버스 일 떄
            for i in range(A, B + 1, 2):
                bus[i] += 1
        elif tp == 3:                           # 광역 버스 일 때
            if A % 2:                           # 출발 정류장이 홀수 일 때
                for i in range(A, B + 1):
                    if i % 3 == 0 and i % 10:
                        bus[i] += 1
            else:                               # 출발 정류장이 짝수 일 떄
                for i in range(A, B + 1):
                    if i % 4 == 0:
                        bus[i] += 1

    print(f'#{tc}', max(bus))
