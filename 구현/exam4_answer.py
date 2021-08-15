n, m = map(int, input().split())

# 방문한 위치 확인을 위한 list 생성
d = [[0] * m for _ in range(n)]

x, y, w = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn():
    global w
    w -= 1
    if w == -1:
        w = 3

# 시뮬레이션 시작
answer = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn()
    # 정면 좌표
    nx = x + dx[w]
    ny = y + dy[w]

    # 가보지 않은 칸이라면 앞으로 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        answer += 1
        turn_time = 0
        continue

    # 앞으로 이동할 수 없는 경우
    else:
        turn_time += 1
    # 네 방향 모두 이동할 수 없는 경우
    if turn_time == 4:
        nx = x - dx[w]
        ny = y - dy[w]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다인 경우
        else:
            break
        # 회전 수 초기화
        turn_time = 0

print(answer)