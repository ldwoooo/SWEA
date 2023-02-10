def row(arr):
    '''
    가로줄 확인 함수
    '''
    for i in range(len(arr)):
        if len(set(arr[i])) == 9:       # set를 이용해 중복되는 숫자 확인
            pass
        else:
            return False
    return True


def column(arr):
    '''
    세로줄 확인 함수
    '''
    na = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            na.append(arr[j][i])

        if len(set(na)) == 9:
            na = []
            pass
        else:
            return False

    return True


def matrix(arr):
    '''
    1~9까지 각각 3X3 매트릭스 확인함수
        1|2|3
        4|5|6
        7|8|9
    '''
    na = []
    # 1
    for a in range(3):
        for b in range(3):
            na.append(arr[a][b])

    if len(set(na)) == 9:
        na = []
        pass
    else:
        return False

    # 2
    for a in range(3):
        for c in range(3, 6):
            na.append(arr[a][c])
    if len(set(na)) == 9:
        na = []
        pass
    else:
        return False

    # 3
    for a in range(3):
        for d in range(6, 9):
            na.append(arr[a][d])
    if len(set(na)) == 9:
        na = []
        pass
    else:
        return False

    # 4
    for e in range(3, 6):
        for f in range(3):
            na.append(arr[e][f])
    if len(set(na)) == 9:
        na = []
        pass
    else:
        return False

    # 5
    for e in range(3, 6):
        for g in range(3, 6):
            na.append(arr[e][g])
    if len(set(na)) == 9:
        na = []
        pass
    else:
        return False

    # 6
    for e in range(3, 6):
        for h in range(6, 9):
            na.append(arr[e][h])
    if len(set(na)) == 9:
        na = []
        pass
    else:
        return False

    # 7
    for i in range(6, 9):
        for j in range(3):
            na.append(arr[i][j])
    if len(set(na)) == 9:
        na = []
        pass
    else:
        return False

    #8
    for i in range(6, 9):
        for k in range(3, 6):
            na.append(arr[i][k])
    if len(set(na)) == 9:
        na = []
        pass
    else:
        return False

    # 9
    for i in range(6, 9):
        for l in range(6, 9):
            na.append(arr[i][l])
    if len(set(na)) == 9:
        pass
    else:
        return False

    return True

# 입력부분
T = int(input())

for tc in range(1, T + 1):
    arr =[list(map(int, input().split())) for _ in range(9)]

    if row(arr) and column(arr) and matrix(arr):
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)

#---------------------------------------------------------------------------------
# 간단하게 줄일 수 있는 방법 (혜진님 코드)

def transpose(arr): #열 체크를 위한 전치행렬 구하기
    row = 9
    col = 9
    arr_T = [[0]*9 for _ in range(9)]

    for i in range(row):
        for j in range(col):
            arr_T[j][i] = arr[i][j]
    return (arr_T)

def check():
    #행 체크
    for i in range(size):
        if len(set(arr[i])) != 9:  #중복 제거하고 크기를 확인했을 때 9가 나와야 모든 숫자가 있는 것
            return 0
    #열 체크
    arr_T = transpose(arr)
    for i in range(size):
        if len(set(arr_T[i])) != 9:
            return 0
    #박스 체크       
    for i in range(0, 9, 3):    #0부터 9까지 3씩 증가 -> 0 3 6
        for j in range(0, 9, 3):
            box = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(box)) != 9:
                return 0
    return 1


T = int(input()) 
for test_case in range(1, T + 1):
    size = 9
    arr = [list(map(int, input().split())) for _ in range(size)]

    ans = check()

    print (f"#{test_case} {ans}")
