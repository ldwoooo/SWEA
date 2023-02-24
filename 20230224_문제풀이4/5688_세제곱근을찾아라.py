T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ''' N = 64일 때,
    X = round(N**(1/3))                 # X = 4
    if X == int(X):                     # 4 == 4 -> True
    
    X = N**(1/3)                        # X = 3.99999999996
    if round(X, 2) == int(X):           # 4 == 3 -> False

    '''
    X = N ** (1 / 3)
    if round(X, 2) == round(X):
        print(f'#{tc}', round(X))
    else:
        print(f'#{tc}', -1)
# --------------------------------------------------------------------------
# 성구 코드
arr = [0] * (10 ** 6 + 1)
for i in range(1, 10 ** 6 + 1):
    arr[i] = i ** 3

for test_case in range(1, int(input()) + 1):
    N = int(input())
    print(f'#{test_case}', end=' ')
    if N == 1:
        print(1)
    elif 1 < N < 8:
        print(-1)
    else:
        for i in range(len(arr)):
            if arr[i] == N:
                print(i)
                break
        else:
            print(-1)
