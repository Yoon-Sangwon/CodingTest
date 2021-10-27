# 2차원 리스트(인접 행렬) 방식 예제
INF = 999999999 # 무한 비용
graph_ = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph_)

print("------------------------")
# 인접 리스트 방식 예제
graph = [[] for _ in range(3)]
print(graph)

# 0은 1과 7로 연결되어 있고 2와 5로 연결되어 있다.
graph[0].append((1,7))
graph[0].append((2,5))
print(graph)

# 1은 0과 7로 연결되어 있다.
graph[1].append((0,7))
print(graph)

# 2은 0과 5로 연결되어 있다.
graph[2].append((0,5))
print(graph)