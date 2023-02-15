for tc in range(1, 11):
    N = int(input())
    problem = list(input())

    nums = []
    plus = []

    for i in problem:
        # 숫자면
        if i.isdigit():
            if len(nums) == 0:
                nums.append(i)
            else:
                x = int(nums.pop())
                p = plus.pop()
                if p == '+':
                    nums.append(x + int(i))
        # 숫자가 아니면
        else:
            plus.append(i)

    print(f'#{tc}', *nums)