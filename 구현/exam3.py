word = input()
ylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x, y = int(word[1]), ylist.index(word[0]) + 1

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

answer = 8
cnt = 0
for i in range(len(dx)):
    xm = x + dx[i]
    ym = y + dy[i]
    if (xm < 1) or (xm >8) or (ym < 1) or (ym >8):
        cnt += 1

print(answer - cnt)