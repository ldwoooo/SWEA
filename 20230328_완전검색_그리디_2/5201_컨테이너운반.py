T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))     # 화물 무게
    t = list(map(int, input().split()))     # 트럭 적재용략

    w.sort(reverse=True)                    # 내림차순 정렬
    t.sort(reverse=True)

    ans = i = cnt_w = cnt_t = 0             # 누적합, 트럭 인덱스, 화물과 트럭 개수
    while True:
        if cnt_w == N or cnt_t == M:        # 화물을 다 실거나 실을 트럭이 없으면 종료
            break

        nw = w.pop(0)                       # 무거운 화물 순으로 꺼낸다
        nt = t[i]
        if nw <= nt:                        # 화물에 실을 수 있으면
            ans += nw                       # 화물 실고 다음 트럭 가져와
            i += 1
            cnt_t += 1                      # 나간 트럭 개수 세기

        cnt_w += 1                          # 실은 화물 개수 세기

    print(f'#{tc}', ans)


