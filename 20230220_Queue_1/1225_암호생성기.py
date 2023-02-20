for tc in range(1, 11):
    N = input()
    nums = list(map(int, input().split()))

    while True:
        for i in range(1, 6):
            a = nums.pop(0) - i                 # 맨 앞 숫자 꺼내고 1~5 순으로 빼기

            if a > 0:                           # 0보다 크면 그대로 넣고 아니면 0 넣기
                nums.append(a)
            else:
                nums.append(0)
                break
        if a <= 0:                              # 0보다 작으면 반복문 종료
            break

    print(f'#{tc}', *nums)

