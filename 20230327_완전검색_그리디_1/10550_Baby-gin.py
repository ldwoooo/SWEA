def run_check(x):               # run check 함수
    if len(set(x)) == 1:        # run 은 3개의 수가 같은 것이므로 set 을 이용해 길이가 1이 되면 합격
        return True
    return False


def triplet_check(x):           # triplet check 함수 (미리 sort 가 된 상태)
    for i in range(2):          # 3개의 수를 돌면서 뒤의 나오는 수가 1이 더 크다면
        if int(x[i]) == int(x[i + 1]) - 1:
            continue
        return False            # 조건을 만족하지 못하면 실패
    return True                 # 조건을 만족해서 통화해서 오면 합격


T = int(input())

for tc in range(1, T + 1):
    num = list(input())
    
    if triplet_check(num[:3]) and triplet_check(num[3:]):           # 123123과 같은 경우를 걸러주기 위한 조건
        print(f'#{tc}', 'Baby Gin')
        
    else:                                                       
        num.sort()

        if run_check(num[:3]) and triplet_check(num[3:]):           # 앞의 3개가 run, 뒤의 3개가 triplet
            print(f'#{tc}', 'Baby Gin')
        elif run_check(num[3:]) and triplet_check(num[:3]):         # 앞의 3개가 triplet, 뒤의 3개가 run
            print(f'#{tc}', 'Baby Gin')
        elif run_check(num[:3]) and run_check(num[3:]):             # 모두 run
            print(f'#{tc}', 'Baby Gin')
        elif triplet_check(num[:3]) and triplet_check(num[3:]):     # 모두 triplet
            print(f'#{tc}', 'Baby Gin')
        else:
            print(f'#{tc}', 'Lose')
