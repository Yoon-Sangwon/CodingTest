N, M = map(int, input().split())
result = 0
for i in range(N):
    data = list(map(int, input().split()))
    value_min = min(data)
    result = max(value_min, result)
print(result)