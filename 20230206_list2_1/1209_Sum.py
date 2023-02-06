def line(x):
    '''
    각 행의 합에서 최대값을 구하는 함수
    '''

    sum_line_arr = []

    # 행(i)를 고정하고 열(j)를 반복하며 각 자리의 수의 합을 구한 후 최댓값을 반환한다
    for i in range(100):
        sum_line = 0

        for j in range(100):
            sum_line += x[i][j]
        sum_line_arr.append(sum_line)

    return max(sum_line_arr)


def row(x):
    '''
    각 열의 합에서 최댓값을 구하는 함수
    '''

    sum_row_arr = []

    # 열(j)를 고정하고 행(i)를 반복하며 각 자리의 수의 합을 구한 후 최댓값을 반환한다
    for j in range(100):
        sum_row = 0

        for i in range(100):
            sum_row += x[i][j]
        sum_row_arr.append(sum_row)

    return max(sum_row_arr)


def cross(x):
    '''
    대각선의 합에서 최댓값 구하는 함수
    '''

    sum_cross = 0
    # 행렬의 가운데 값이 첫 번째 조건문에서 빠지기 때문에 미리 넣어준다
    sum_cross2 = arr[50][50]

    for i in range(100):
        for j in range(100):

            # 왼쪽 위에서 오른쪽 아래 방향의 대각선
            if i == j:
                sum_cross += x[i][j]

            # 오른쪽 위에서 왼쪽 아래 방향의 대각선
            elif i + j == 99:
                sum_cross2 += x[i][j]

    return max([sum_cross, sum_cross2])


for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 각 함수의 최댓값 중 최종적인 최댓값
    result = max(line(arr), row(arr), cross(arr))

    print(f'#{tc}', result)

# ---------------------------------------------------------------------------------
# 구민석님 코드

for _ in range(10):

    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum3 = sum4 = 0
    totalsum = []
    for i in range(100):
        sum1 = sum2 = 0
        for j in range(100):
            sum1 += arr[i][j]
            sum2 += arr[j][i]
        totalsum.append(sum1)
        totalsum.append(sum2)

    for i in range(100):
        sum3 += arr[i][i]
    totalsum.append(sum3)

    for i in range(100):
        sum4 += arr[i][4 - i]
    totalsum.append(sum4)

    ans = max(totalsum)

    print("#{} {}".format(T, ans))