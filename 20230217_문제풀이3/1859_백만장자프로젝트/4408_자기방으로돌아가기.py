T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    # nr = []
    # for a in room:
    #     a.sort()
    #     nr.append(a)
    #
    # nr.sort()
    time = 0
    for i in range(N-1, -1, -1):
        stack = []
        if room[i][0] not in range(room[i - 1][0], room[i - 1][1] + 2):
            room.pop(i)


    print(room)
    # print(f'#{tc}', len(room))