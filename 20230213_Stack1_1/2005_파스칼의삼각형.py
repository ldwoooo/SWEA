# 2차원배열
T = int(input())

for tc in range(1, T+1):
    n = int(input())

    # 파스칼의 삼각형 구하기
    tri = [[0] * r for r in range(1, n + 1)]

    print(f'#{tc}')
    # 한줄씩 구하면서 출력,
    # 이전 행에서 사용했던 결과를 이용해서 현재 행을 구하기
    for r in range(n):
        for c in range(r + 1):
            if c == 0:
                tri[r][c] = 1
            elif r == c:
                tri[r][c] = 1
            else:
                tri[r][c] = tri[r - 1][c - 1] + tri[r - 1][c]
        print(*tri[r])

# 스택
T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    # 첫번째 줄
    tri = [1]
    print(f'#{tc}')
    print(*tri)

    # 두번째 줄부터 스택을 사용해서 삼각형만들기
    for i in range(n - 1):
        # 현재줄의 맨 처음과 끝에 있는 1은 더할게 없으니 0으로 채워준다.
        stack = [0] + tri + [0]
        tri = []    # 해당 줄에서 사용할 숫자를 저장할 리스트

        # pop()을 하면 최근에 사용했던 값을 가져올 수 있다.
        num = stack.pop()   # 자신의 오른쪽 위 숫자 가져오기

        while stack:    # stack 이 비어있을 때까지
            num2 = stack.pop()  # 왼쪽 위 숫자 가져오기
            tri.append(num + num2)

            num = num2  # 자신의 오른쪽 숫자를 왼쪽 숫자로 바꿔준다.

        print(*tri)
