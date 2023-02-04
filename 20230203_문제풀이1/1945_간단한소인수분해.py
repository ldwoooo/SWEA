T = int(input())

for tc in range(1, T + 1):
    num = int(input())
    # 나누는 숫자들, 내림차순으로 리스트 생성
    divisible_num = [11, 7, 5, 3, 2]
    result = []

    for i in divisible_num:

        count = 0

        while True:
            # 큰 숫자부터 나눠서 0이 되면 count ++, num 재정의
            if num % i == 0:
                count += 1
                num = num // i
            # 0이 아니면 result 리스트 0번 리스트에 count 값 넣기
            else:
                result.insert(0, count)
                break

    print(f'#{tc}', *result)