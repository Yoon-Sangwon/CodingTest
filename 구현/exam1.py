N = int(input())
cmds = list(input().split())

X, Y = 1, 1
move = ['R', 'L', 'D', 'U']
dX = [0, 0, 1, -1]
dY = [1, -1, 0, 0]

for cmd in cmds:
    for i in range(len(move)):
        if cmd == move[i]:
            cx = X + dX[i]
            cy = Y + dY[i]
    if (cx < 1) or (cy < 1) or (cx > N) or (cy > N):
        continue
    
    X = cx
    Y = cy

print(X, Y)