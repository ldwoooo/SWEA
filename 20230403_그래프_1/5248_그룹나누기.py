def findset(i):
    while rep[i] != i:
        i = rep[i]
    return i
 
 
def union(x, y):
    rep[findset(y)] = findset(x)
 
 
T = int(input())
 
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    rep = [i for i in range(N + 1)]
 
    for i in range(0, len(arr) - 1, 2):
        t, f = arr[i], arr[i + 1]
        union(t, f)
 
    cnt = 0
    for k in range(1, len(rep)):
        if k == rep[k]:
            cnt += 1
 
    print(f'#{tc}', cnt)