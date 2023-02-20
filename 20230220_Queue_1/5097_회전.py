def dequeue():
    front = 0
    return nums[front]


def enqueue(data):
    rear = N - 1
    nums[rear] = data


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    for _ in range(M):
        a = dequeue()                       # 맨 앞 숫자 꺼낸다
        for i in range(N - 1):      # nums의 남은 숫자들 앞으로 한자리씩 땡겨온다
            nums[i] = nums[i+1]
        enqueue(a)                          # 맨 뒤로 보낸다

    print(f'#{tc}', nums[0])

# ----------------------------------------------------------------------------
# 성구 코드
def enqueue(item):
    global rear
    rear += 1
    arr[rear] = item


def dequeue():
    global front
    front += 1
    return arr[front - 1]


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split())) + [0] * M
    rear = N - 1
    front = 0

    for i in range(M):
        enqueue(dequeue())

    print(f'#{test_case} {arr[front]}')