N, M, K = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

a = x[-1]
b = x[-2]

answer = 0
answer += (a * K + b) * (M // (K + 1)) + a * (M % (K + 1))
print(answer)