for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(10)]

    di = [1, 0, 0]  # 상, 좌, 우
    dj = [0, -1, 1]

    print(arr)