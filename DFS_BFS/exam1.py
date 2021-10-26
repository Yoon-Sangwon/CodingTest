# 큐(Queue) 예제

from collections import deque
queue = deque()

queue.append(5)
print(queue)
queue.append(2)
print(queue)
queue.append(3)
print(queue)
queue.append(7)
print(queue)
queue.popleft()
print(queue)
queue.append(1)
print(queue)
queue.append(4)
print(queue)
queue.popleft()

# 먼저 들어온 순서대로 출력
print(queue)
# 나중에 들어온 순서대로 출력
queue.reverse()
print(queue)