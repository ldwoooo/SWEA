for test_case in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))

    view_list = 0
    for i in range(N - 4):
        maxV = 0
        maxV_2nd = 0

        for j in range(i, i + 5):
            if maxV < height[j]:
                maxV = height[j]
            for k in range(2, N - 2):
                if maxV == height[k]:
                    for j in range(i, i + 5):
                        if maxV_2nd < height[j] and i + 2 != j:
                            maxV_2nd = height[j]
        view = maxV - maxV_2nd
        view_list += view

    print(f'#{test_case}', view_list)
# ---------------------------------------------------------------
# 혜진님 코드
for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
 
    count = 0
     
    for i in range(N-4):
        maxV = 0
        subV = 0
        for j in range(i, i+5):
            if maxV < arr[j] and i + 2 != j:
                maxV = arr[j]
                
        if maxV < arr[i+2]:
            count += (arr[i+2] - maxV)
 
    print(f'#{test_case} {count}')