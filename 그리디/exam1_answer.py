N, M, K = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

a = x[-1]
b = x[-2]

answer = 0
while True:
    for i in range(K):
        if M == 0:
            break
        answer += a
        M -= 1
#        if M == 0:
#            break
    if M == 0:
        break
    answer += b
    M -= 1
#    if M == 0:
#        break

print(answer)