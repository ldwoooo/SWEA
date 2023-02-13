def my_push(data):
    stack.append(data)


def my_pop():
    return stack.pop()


T = int(input())

for tc in range(1, T + 1):
    txt = input()

    stack = []

    for i in txt:
        if len(stack) == 0:         # stack이 비어있으면 넣어주세요
            my_push(i)
        elif i != stack[-1]:        # 새로운 문자와 stack의 마지막 문자가 다르면 넣어주세요
            my_push(i)
        else:                       # 새로운 문자와 stack의 마지막 문자가 같으면 빼주세요
            my_pop()

    print(f'#{tc}', len(stack))
