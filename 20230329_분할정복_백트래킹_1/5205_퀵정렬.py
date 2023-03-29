def hoare(arr, l, r):
    p = arr[l]                              # 맨 왼쪽 기준
    i = l                                   # 왼쪽에서부터 피봇보다 큰 값을 찾아 오른쪽으로 이동
    j = r                                   # 오른쪽에서부터 피봇보다 작은 값을 찾아 왼쪽으로 이동
    while i <= j:                           # i와 j가 교차할 때까지
        while i <= j and p >= arr[i]:       # i와 j가 교차하지 않고 큰 값을 찾을 때까지 i ++
            i += 1
        while i <= j and p <= arr[j]:       # i와 j가 교차하지 않고 작은 값을 찾을 때까지 j --
            j -= 1
        if i < j:                           # 교차하지 않았다면
           arr[i], arr[j] = arr[j], arr[i]  # i 위치 값과 j 위치의 값 교환
    arr[l], arr[j] = arr[j], arr[l]         # 교차했다면 피봇값과 j 위치의 값 교환
    return j


def qsort(arr, l, r):
    if l < r:
        s = hoare(arr, l, r)                # 정렬된 피봇의 위치
        qsort(arr, l, s - 1)                # 움직인 피봇, 고정점을 중심으로 왼쪽 퀵정렬
        qsort(arr, s + 1, r)                # 고정점을 중심으로 오른쪽 퀵정렬


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    L = list(map(int, input().split()))
    qsort(L, 0, N - 1)
    print(f'#{tc}', L[N // 2])
