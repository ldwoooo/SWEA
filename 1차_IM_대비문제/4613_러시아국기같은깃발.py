def White(x, M):
    global count
    for i in range(M):
        if flag[x][i] != 'W':
            count += 1


def Blue(x, M):
    global count
    for i in range(M):
        if flag[x][i] != 'B':
            count += 1


def Red(x, M):
    global count
    for i in range(M):
        if flag[x][i] != 'R':
            count += 1


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    count = 0

    # # 두번 째 줄은 White or Blue
    # count_W, count_B, count_R = 0, 0, 0
    # for i in range(M):
    #     if flag[1][i] == 'W':
    #         count_W += 1
    #     elif flag[1][i] == 'B':
    #         count_B += 1
    #
    # if count_W > count_B:
    #     White(1)
    # else:
    #     Blue(1)
    #
    # # 마지막에서 두번 째 줄은 Blue or Red
    # for i in range(M):
    #     if flag[N - 2][i] == 'W':
    #         count_W += 1
    #     elif flag[N - 2][i] == 'B':
    #         count_B += 1


    White(0, M)
    Red(N - 1, M)
    print(count)