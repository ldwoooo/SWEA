def run_check(arr):
    cnt = 0
    for k in arr:
        if cnt == 3:
            return True
        if k:                                   # 카드가 있으면 cnt ++ 해주고 연속된 3개이면 참을 반환
            cnt += 1
        else:
            cnt = 0

    if cnt == 3:                                # 1번이 마지막 카드 3장이 7, 8, 9일 때 참을 보내주기 위한 코드
        return True                             # 마지막이 9이면 return 을 거치지 못하고 for 문이 끝나기 때문
    return False


def triplet_check(arr):
    for k in arr:
        if k >= 3:                              # 카드의 누적이 3장 이상이면 참을 반환
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    ans = 0                                             # 초기화 위치!!!!!!
    card = list(map(int, input().split()))

    player1 = [0] * 10
    player2 = [0] * 10
    for i in range(12):
        if i % 2:                                               # 홀수번째 카드는 player2에게
            player2[card[i]] += 1
            if run_check(player2) or triplet_check(player2):    # run, triplet 검사 중 하나라도 참이면
                ans = 2                                         # player2 승                            
                print(f'#{tc}', 2)  
                break
        else:
            player1[card[i]] += 1                               # 짝수번째 카드는 player1에게
            if run_check(player1) or triplet_check(player1):    # 검사중 하나라도 참이면 player1 승
                ans = 1
                print(f'#{tc}', 1)
                break
    if ans == 0:                                        # 무승부이면, ans = 0이면 무승부
        print(f'#{tc}', 0)