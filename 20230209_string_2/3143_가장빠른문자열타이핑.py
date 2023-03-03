T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()
    i = 0
    count = 0
    while i <= len(A) - 1:
        if A[i: i + len(B)] == B:
            count += 1
            i += len(B)
        else:
            i += 1
            count += 1

    print(f'#{tc}', count)

