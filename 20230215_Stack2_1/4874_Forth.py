def addtion(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x // y


T = int(input())

for tc in range(1, T + 1):
    code = list(input().split())

    stack = []
    for i in code:
        if i.isdigit():
            stack.append(i)

        elif i == '+':
            # stack 에는 숫자가 2개 이상 있어야 연산이 가능하다
            if len(stack) >= 2:
                y = int(stack.pop())
                x = int(stack.pop())

                result = addtion(x, y)
                stack.append(result)
            else:
                print(f'#{tc}', 'error')
                break

        elif i == '-':
            if len(stack) >= 2:
                y = int(stack.pop())
                x = int(stack.pop())

                result = subtraction(x, y)
                stack.append(result)
            else:
                print(f'#{tc}', 'error')
                break

        elif i == '*':
            if len(stack) >= 2:
                y = int(stack.pop())
                x = int(stack.pop())

                result = multiplication(x, y)
                stack.append(result)
            else:
                print(f'#{tc}', 'error')
                break

        elif i == '/':
            if len(stack) >= 2:
                y = int(stack.pop())
                x = int(stack.pop())

                result = division(x, y)
                stack.append(result)
            else:
                print(f'#{tc}', 'error')
                break

        elif i == '.':
            if len(stack) == 1:
                print(f'#{tc} {stack.pop()}')
            else:
                print(f'#{tc}', 'error')

# -----------------------------------------------------------------------------------------------------
# 깔끔한 체련님 코드
def Forth(arr):
    op = ['*', '/', '+', '-', '.']
    stack = []

    while True:
        for s in arr:
            if s not in op:  # 피연산자를 만나면 스택에 넣어라
                stack.append(s)
            else:  # 연산자를 만나면 스택에서 두개를 꺼내서 계산하고 다시 넣어라!
                if s == '.' and len(stack) == 1:
                    return stack.pop()
                elif len(stack) < 2:
                    return 'error'
                else:
                    e2 = int(stack.pop())
                    e1 = int(stack.pop())
                    if s == '*':
                        stack.append(e1 * e2)
                    elif s == '/':
                        stack.append(e1 // e2)
                    elif s == '+':
                        stack.append(e1 + e2)
                    elif s == '-':
                        stack.append(e1 - e2)
        else:
            return 'error'


T = int(input())
for tc in range(1, T + 1):
    arr = input().split()

    answer = Forth(arr)
    print(f'#{tc} {answer}')
