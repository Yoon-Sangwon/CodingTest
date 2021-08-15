n, m = map(int, input().split())
x, y, w = map(int, input().split())

maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

dir = [0, 3, 2, 1]
idx = dir.index(w)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
bx = [1, 0, -1, 0]
by = [0, 1, 0 ,-1]

cnt = 1
move = 0
while True:
    print('----------------------------------')
    # 현재 있는 칸 2로 지정
    print('x :', str(x), 'y :', str(y))
    maps[x][y] = 2

    # 왼쪽 방향 좌표를 ddx ddy로 임시 설정
    ddx = x + dx[idx]
    ddy = y + dy[idx]
    
    print('ddx :', str(ddx), 'ddy :', str(ddy))
    print('왼쪽방향 : ', str(maps[ddx][ddy]))
    # 왼쪽 방향 좌표가 육지인 경우
    if maps[ddx][ddy] == 0:
        # 방향 전환 후
        idx += 1
        if idx > 3:
            idx -= 4
        # 해당 칸으로 전진 및 방문한 칸수 증가 및 방향전환 초기화
        x = ddx
        y = ddy
        cnt += 1
        move = 0
        continue
    # 왼쪽 방향 좌표가 육지가 아닌 경우
    else:
        # 방향만 전환시켜줌
        idx += 1
        if idx > 3:
            idx -= 4
        move += 1
    print('index :', str(idx))
    print('move :', str(move))
    # 모든 방향으로 전환했는데 움직일 칸이 없는 경우
    if move == 4:
        move = 0
        ddx = x + bx[idx]
        ddy = y + by[idx]
        if maps[ddx][ddy] == 1:
            break
        else:
            x = ddx
            y = ddy

print(cnt)