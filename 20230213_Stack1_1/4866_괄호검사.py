T = int(input())

for tc in range(1, T + 1):
    txt = input()

    stack = [0] * 100           # 입력이 100 글자 이내
    top = -1
    ans = 1

    for x in txt:               # 한 글자씩 가져오기

        if x == '(':            # 여는 괄호 push
            top += 1
            stack[top] = x

        elif x == '{':
            top += 1
            stack[top] = x

        elif x == '}':
            if top > -1:
                if stack[top] == '{':
                    top -= 1
                else:
                    ans = 0
            else:
                ans = 0

        elif x == ')':                      # 닫는 괄호인 경우
            if top > -1:                    # 스택에 여는 괄호가 있으면
                if stack[top] == '(':       # 동시에 괄호가 '(' 이면
                    top -= 1                # pop()
                else:                       # '('가 아니면 오류
                    ans = 0
            else:                           # 스택에 여는 괄호가 없으면
                ans = 0                     # 오류

    else:                                   # txt 끝

        if top > -1:                        # 여는 괄호가 남아있으면
            ans = 0                         # 오류
        # else:
        #     ans = 1                       # 정상(default)

    print(f'#{tc}', ans)

# --------------------------------------------------------------------------
# 함수 사용
def my_push(data):
    stack.append(data)


def my_pop():
    return stack.pop()


T = int(input())

for tc in range(1, T + 1):

    txt = input()
    stack = []
    ans = 1
    for x in txt:
        if x == '(':
            my_push(x)
        elif x == '{':
            my_push(x)
        elif x == '}':
            if len(stack) > 0 and stack[-1] == '{':
                my_pop()
            else:
                ans = 0
        elif x == ')':
            if len(stack) > 0 and stack[-1] == '(':
                my_pop()
            else:
                ans = 0
    else:
        if len(stack):
            ans = 0

    print(f'#{tc}', ans)