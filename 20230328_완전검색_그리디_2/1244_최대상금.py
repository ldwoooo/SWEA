# 교수님 풀이
def f(i, k, c):             # i 현재 교환획수, k 주어진 횟수, c 카드 수
    global maxV
    if i == k:              # 남은 교화횟수가 없으면
        tmp = int(''.join(card))
        if maxV < tmp:
            maxV = tmp
    else:
        for p in range(c - 1):
            for q in range(p + 1, c):
                card[p], card[q] = card[q], card[p]
                tmp = int(''.join(card))
                if tmp not in v[i]:     # 같은 교환 횟수에 같은 숫자가 나오면 중복 과정 생략
                    v[i].append(tmp)
                    f(i + 1, k, c)      # 다음 교환
                card[p], card[q] = card[q], card[p]     # 다른 p, q를 선택하기 위해 원상 복구


T = int(input())

for tc in range(1, T + 1):
    num, N = input().split()
    card = list(num)
    N = int(N)

    # print(card, N)
    maxV = 0
    v = [[] for _ in range(N)]      # 교환횟수 별로 만들어지는 숫자를 저장
    f(0, N, len(card))
    print(f'#{tc}', maxV)
