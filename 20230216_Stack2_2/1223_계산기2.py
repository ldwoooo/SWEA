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
                new_txt += stack.pop()

            else:
                stack.append(i)

    while stack:
        new_txt += stack.pop()

    return new_txt



# def cal():



for tc in range(1, 2):
    n = int(input())
    formula = list(input())

    # 후위 표기식
    new_formula = change(formula)
    # 계산
    # result = cal(new_formula)

    print(new_formula)