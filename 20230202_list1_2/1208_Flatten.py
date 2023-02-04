for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    maxV_id = 0
    minV_id = 0

    while True:
        # 빼진 최댓값과 더해진 최솟값 뽑는다
        for i in range(len(boxes)):
            if boxes[maxV_id] < boxes[i]:
                maxV_id = i
            if boxes[minV_id] > boxes[i]:
                minV_id = i

        if dump == 0:
            print(f'#{tc}', boxes[maxV_id] - boxes[minV_id])
            break

        # 다시 최대,최소값을 뽑는다
        for i in range(len(boxes)):
            if boxes[maxV_id] < boxes[i]:
                maxV_id = i
            if boxes[minV_id] > boxes[i]:
                minV_id = i

        # 최대값에 1을 빼주고 최소값의 1을 더해준
        boxes[maxV_id] -= 1
        boxes[minV_id] += 1
        dump -= 1