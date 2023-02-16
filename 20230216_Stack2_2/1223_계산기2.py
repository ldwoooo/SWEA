def change(txt):
    new_txt = ""
    stack = []

    op = {'+': 1, '*': 2}

    for i in txt:
        # 숫자면 결과에 저장
        if i.isdigit():
            new_txt += i
        # 연산자이면 스택에 저장
        else:
            if stack and op[stack[-1]] > op[i]:
                while stack:
                    new_txt += stack.pop()
                stack.append(i)

            else:
                stack.append(i)
                
            # 뭐가 다른지 생각해보기
            # 아마 *이 연속되는 부분에서 오류가 떴는데 그 차이에 대해서 생각해보자 
            # while stack and op[stack[-1]] >= op[i]:
            #     new_txt += stack.pop()
            #
            # stack.append(i)

    while stack:
        new_txt += stack.pop()

    return new_txt


def cal(txt):

    op = ['+', '*']
    stack = []

    for i in txt:
        # 숫자면 스택에 쌓기
        if i.isdigit():
            stack.append(i)

        # 연산자면 숫자 꺼내서 계산
        elif i in op and len(stack) >= 2:
            y = int(stack.pop())
            x = int(stack.pop())

            if i == '+':
                num = x + y
                stack.append(num)

            elif i == '*':
                num = x * y
                stack.append(num)
        else:
            return

    return stack[-1]


for tc in range(1, 11):
    n = int(input())
    formula = list(input())

    # 후위 표기식
    new_formula = change(formula)
    # 계산
    result = cal(new_formula)

    # print(new_formula)
    print(f'#{tc}', result)