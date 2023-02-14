def color_paper(n):
    '''
    만들 수 있는 가지수 구하는 재귀함수
    2의 n제곱 - 전 차례 값 ;이라는 규칙을 이용
    '''

    if n == 0 :             # n이 0일 때, 초기값은 1
        return 1

    return 2 ** n - color_paper(n-1)


T = int(input())

for tc in range(1, T+1):
    num = int(input())

    print(f'#{tc}', color_paper(num // 10))     # 길이가 10의 배수이므로 10으로 나눠서 출력

# -------------------------------------------------------------------------
# 반복문

T = int(input())

for tc in range(1, T + 1):
    num = int(input())

    a = [[0] * n for n in range(num//10 + 1)]
    a[0] = 1

    for i in range(1, num//10 + 1):
        a[i] = (2 ** i) - a[i-1]
    print(f'#{tc}', a[i])

