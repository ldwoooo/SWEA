
T = int(input())

nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(1, T + 1):
    tc, N = input().split()
    arr = list(input().split())

    num_dict = {}
    for i in nums:                  # 딕셔너리에는 순서가 없기 때문에 굳이 생각해주지 않아도 됨.
        num_dict[i] = 0

        for j in arr:               # 언어의 개수를 센다
            if i == j:
                num_dict[i] += 1

    print(tc)
    for k in nums:
        print((k + ' ') * num_dict.get(k))

