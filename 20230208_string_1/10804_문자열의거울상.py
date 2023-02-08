T = int(input())

for tc in range(1, T + 1):
    word = input()

    nw = word.replace('b', '1')
    nw = nw.replace('d', '2')
    nw = nw.replace('q', '3')
    nw = nw.replace('p', '4')
    nw = nw.replace('1', 'd')
    nw = nw.replace('2', 'b')
    nw = nw.replace('3', 'p')
    nw = nw.replace('4', 'q')
    nw = nw[::-1]

    print(f'#{tc}', nw)
