T = int(input())

for tc in range(1, T + 1):
    arr = input()
    arr2 = input()

    if arr in arr2:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)
