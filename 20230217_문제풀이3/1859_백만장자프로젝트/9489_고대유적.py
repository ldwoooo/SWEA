T = int(input())
 
 
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    result = []
    for i in range(N):
        count = 0
        for j in range(M):
            if arr[i][j]:
                count += 1
            else:
                result.append(count)
                count = 0
        result.append(count)
 
    for j in range(M):
        count = 0
        for i in range(N):
            if arr[i][j]:
                count += 1
            else:
                result.append(count)
                count = 0
        result.append(count)
 
    print(f'#{tc}', max(result))

# -----------------------------------------------------------------------
T = int(input())
  
  
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
  
    length = []
    count = 0
  
    for a in range(N):
        count = 0
        for b in range(M):
            if arr[a][b] == 1:
                count += 1
            else:
                count = 0
  
            if count:
                length.append(count)
  
    count = 0
  
    for b in range(M):
        count = 0
        for a in range(N):
            if arr[a][b] == 1:
                count += 1
            else:
                count = 0
  
            if count:
                length.append(count)
  
    print(f'#{tc}', max(length))