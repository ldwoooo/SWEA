T = int(input())

for tc in range(1, T + 1):                          # 입력
    N, M = map(int, input().split())
    nums = [input() for _ in range(N)]

    code = {                                        # 암호화 규칙
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }

    q = []
    i, j = N - 1, M - 1                             # 뒤에서부터 탐색하기 위한 초기값
    while True:

        if nums[i][j] == '1':                       # 1을 만나면
            for k in range(-55, 1):                 # 56줄의 암호를 q에 넣는다
                q.append(nums[i][j + k])
            break
        else:                                       # 0이면
            j -= 1                                  # j -- 하면서 탐색
            if j < 0:                               # j가 0이 되면 j 초기화하고 행 바꿔줘
                i -= 1
                j = M - 1
    # print(q)

    result = []
    for i in range(0, 56, 7):                       # q를 7개씩 끊어 돌면서
        password = ''
        for j in range(i, i + 7):
            password += q[j]
        a = code.get(password)                      # 암호화 규칙에 맞는 숫자를 찾아서
        result.append(a)                            # 결과 리스트에 넣어줘
        # print(password)
    # print(result)

    odd, even = 0, 0                                # 짝수, 홀수 합
    for i in range(0, 8, 2):
        odd += result[i]
    for j in range(1, 9, 2):
        even += result[j]
    # print(odd, even)

    if (odd * 3 + even) % 10 == 0:                  # 올바른 암호인지 판별
        print(f'#{tc}', sum(result))
    else:
        print(f'#{tc}', 0)