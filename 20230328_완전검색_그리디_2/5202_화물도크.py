T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]

    time.sort(key=lambda x: x[1])           # 종료시간을 기준으로 정렬

    cnt = 1
    s_tmp, e_tmp = time.pop(0)              # 가장 일찍 끝나는 작업 수행
    while time:                             # 신청서가 남아있을 때 까지
        s, e = time.pop(0)
        if s >= e_tmp:                      # 이전 종료 시간보다 늦게 시작하는 작업이 있으면
            cnt += 1
            s_tmp, e_tmp = s, e             # 해당 작업을 수행한다.

    print(f'#{tc}', cnt)
