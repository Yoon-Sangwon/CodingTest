# import time
N, K = map(int,input().split())
# x = time.time()
answer = 0

while True:
    if N == 1:
        break
    if (N % K) == 0:
        N /= K
        answer += 1
        continue
    N -= 1
    answer += 1

# y = time.time()
# print(y-x)
print(answer)