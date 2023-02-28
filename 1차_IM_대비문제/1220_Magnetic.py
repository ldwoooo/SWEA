for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for i in range(N):                                  # 2차원 배열 돌아보자
        for j in range(N):
            if table[i][j] == 1:                        # N극을 만나면 아래에 S극이 있는지 살펴보자
                tmp = i                                 # 기존 위치를 활용해야하므로 잠시 tmp에 넣어주고
                while True:
                    tmp += 1
                    if tmp > N - 1:                     # 맨 끝에 다다르면 멈춰
                        break
                    elif table[tmp][j] == 2:            # S를 만나면 count 하고 멈춰
                        count += 1
                        break
                    elif table[tmp][j] == 1:            # N을 만나면 그냥 멈춰
                        break

            elif table[i][j] == 2:                      # S극을 만나면 위에 N극이 있는지 살펴보자
                tmp = i
                while True:
                    tmp -= 1
                    if tmp < 0:                         # 맨 위에 다다르면 멈춰
                        break
                    elif table[tmp][j] == 1:            # N극을 만나면 count 하고 멈춰
                        count += 1
                        break
                    elif table[tmp][j] == 2:            # S극을 만나면 그냥 멈춰
                        break

    print(f'#{tc}', count // 2)                 # S극, N극 각각을 탐색했으니까 반으로 나눠줌

# ------------------------------------------------------------------------------------------------
# 성구코드. stack 활용
for test_case in range(1, 11):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]
    count = 0       # 교착 상태 개수    
    for i in range(100):
        stack = []      # 극 확인용 stack      
        for j in range(100):    
            mag = table[j][i]   
            if mag != 0:    # 자성이 있는 아이인가?
                if stack:   # 이전에 자성이 있는 아이가 있었는가?
                    if stack[-1] == mag:    # 있다면 같은 극으로 가는 아이인가?
                        pass        # 같은 아이는 패스
                    else:
                        stack.pop()     # 다른 아이라면 이전꺼 빼내고
                        count += 1      # 교착상태 +1    
                else:                   # 자성이 있는 아이가 없었다면
                    if mag != 2:        # 어느 방향으로 가는아이인가?    
                        stack.append(mag)   # 위에서부터 확인하므로 위로가는 아이는 패스
    print(f'#{test_case} {count}')