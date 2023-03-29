def merge(l, r):            # 병합 과정
    global cnt

    # 병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 cnt ++
    if l[-1] > r[-1]:
       cnt += 1

    ''' 시간 초과가 발생해서 pop 이 아닌 변수를 활용해야한다.
    
    while len(l) > 0 or len(r) > 0:
        if len(l) > 0 and len(r) > 0:
            if l[0] <= r[0]:
                result.append(l.pop(0))
            else:
                result.append(r.pop(0))
        elif len(l) > 0:
            result.append(l.pop(0))
        elif len(r) > 0:
            result.append(r.pop(0))
    '''
    result = []
    nl, nr = 0, 0                           # pop 대신 길이의 제한을 활용하기 위한 변수, index 와 비슷
    while len(l) > nl or len(r) > nr:       # l과 r이 빌 때까지
        if len(l) > nl and len(r) > nr:     # 둘다 비어 있지 않으면
            if l[nl] <= r[nr]:              # 오른쪽 첫 숫자가 왼쪽 첫 숫자보다 크거나 같으면
                result.append(l[nl])        # 왼쪽 첫 숫자를 결과 리스트에 넣는다.
                nl += 1                     # 길이 조건 및 index +1. (해당 숫자를 왼쪽에서 꺼낸다.)
            else:                           # 오른쪽 첫 숫자가 더 작으면 반복.
                result.append(r[nr])
                nr += 1
        elif len(l) > nl:                   # 왼쪽에만 숫자가 남아 있을 경우
            result.append(l[nl])
            nl += 1
        elif len(r) > nr:                   # 오른쪽에만 숫자가 남아 있는 경우
            result.append(r[nr])
            nr += 1

    return result


def msort(arr):                 # 분할 과정
    if len(arr) == 1:           # 원소가 1개만 남으면 반환해준다
        return arr

    middle = len(arr) // 2

    left = arr[0: middle]       # 분할 정복
    right = arr[middle: N]

    left = msort(left)          # 원소가 1개만 남을 때까지 재귀로 돌린다
    right = msort(right)
    return merge(left, right)


T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    L = list(map(int, input().split()))
    cnt = 0
    print(f'#{tc}', msort(L)[N // 2], cnt)
