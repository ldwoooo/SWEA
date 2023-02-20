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

# -----------------------------------------------------------------------------
# queue 로 풀기 (1. 선형큐, 2. 원형큐)

for tc in range(1, 3):
    t = int(input())

    # 문자열 입력
    password = list(map(int, input().split()))
    n = 8
    # 1-1. 일단 size를 엄청 크게 해보자
    q = [0] * 100000
    front = rear = -1
    # 2. 앞에서부터 차례대로 삽입을 한다.
    for i in range(n):
        rear += 1
        q[i] = password[i]

    # 1-2. 원형 큐를 사용한다면
    q = [0] * (n + 1)
    front = rear = 0
    for i in range(n):
        rear = (rear + 1) % n
        q[rear] = password[i]
    # print(rear)
    # 1부터 차례대로 증가하는수
    number = 1

    while True:
        # 일단 하나 꺼내서
        # 1,2,3,..... 증가하는 수로 빼서 다시 큐에 추가
        front = (front + 1) % n
        item = q[front]
        item -= number
        # 빼 봤는데 이 수가 만약 0 이하가 되어버렸다. ==> 비밀번호가 완성되는 순간
        # 그숫자를 0으로 바꾸고 큐의 맨 뒤에 삽입
        if item <= 0:
            item = 0
            rear = (rear + 1) % n
            q[rear] = item
            break
        else:
            # 0이하가 아니라면 그냥 맨 뒤에 넣기
            rear = (rear + 1) % n
            q[rear] = item
            number += 1
            if number > 5:
                number = 1

    print(f"#{tc}", end=" ")
    # 원형 큐를 사용했다면 마지막에서 front 위치를 잘 계산해서 비밀번호를 만들어 주면 된다.
    # print(front)
    # print(q)
    # 그냥 8번 빼면 되지 않을까??
    for i in range(8):
        front = (front + 1) % n
        print(q[front] , end = " ")
    print()
