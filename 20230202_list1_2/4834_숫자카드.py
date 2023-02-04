T = int(input())
 
for ts in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
 
    # 입력 받는 숫자 ai의 최댓값이 9 이므로 10개의 자리 counts 만든다
    counts = [0] * 10
 
    # arr에 들어있는 숫자 카운팅
    for x in arr:
        counts[x] += 1
 
    # counts 리스트에 인덱스를 활용해 최댓값과 인덱스 값 찾기
    maxV_index = 0
 
    for i in range(len(counts)):
        if counts[maxV_index] <= counts[i]:
            maxV_index = i
 
    print(f'#{ts}', maxV_index, counts[maxV_index])