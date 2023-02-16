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

# -----------------------------------------------------------------------
# 교수님 풀이
T = 10


def get_postfix(infix, n):
    postfix = ""
    stack = []

    # i번째 글자에 대해서 연산자면 스택에 넣고 피연산자면 결과에 출력
    for i in range(n):
        # 피연산자 이면 출력
        if "0" <= infix[i] <= "9":
            postfix += infix[i]
        # 연산자였다.
        else:
            # 스택이 비어있지 않으면
            if stack:
                postfix += stack.pop()
            # 연산자 스택에 추가
            stack.append(infix[i])

    # 스택이 빌때까지 남은 연산자를 결과에 출력
    while stack:
        postfix += stack.pop()

    return postfix


def get_result(postfix):
    stack = []

    # 후위 표기식에서 글자를 하나씩 가져와서 계산
    for c in postfix:
        # 피연산자인 경우 스택에 넣기
        if "0" <= c <= "9":
            stack.append(int(c))
        # 연산자인 경우 계산
        else:
            right = stack.pop()
            left = stack.pop()

            # 연산자가 + 하나밖에 없으니까
            result = right + left
            # 다음 연산을 위해서 현재 결과를 스택에 저장
            stack.append(result)

    # 스택에 남은 단 하나의 결과를 pop 해서 출력
    return stack.pop()


for tc in range(1, T + 1):
    n = int(input())
    exp = input()

    # 1. 후위표기식으로 변환
    postfix = get_postfix(exp, n)

    # 2. 후위표기식을 계산
    answer = get_result(postfix)

    print(f"#{tc} {answer}")