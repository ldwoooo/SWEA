def func(P, x):
    '''
    이진 검색으로 숫자를 찾는 횟수를 세는 함수
    '''
    # 문제에 맞춰 검색 구간의 start를 1로 맞춰줌
    start = 1
    count = 1

    while True:

        # middle과 같다면 반복문 중지
        if (int((P + start) / 2)) == x:
            break

        # middle과 end 사이에 있다면 start 바꿔줌
        elif (int((P + start) / 2)) < x < P:
            count += 1
            start = ((P + start) // 2)

        # start와 middle 사이에 있다면 end 바꿔줌
        elif start < x < (int((P + start) / 2)):
            count += 1
            P = (int((P + start) / 2))

    return count


T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = list(map(int, input().split()))

    count_a = func(P, Pa)
    count_b = func(P, Pb)

    if count_a < count_b:
        print(f'#{tc}', 'A')
    if count_a == count_b:
        print(f'#{tc}', 0)
    if count_a > count_b:
        print(f'#{tc}', 'B')
