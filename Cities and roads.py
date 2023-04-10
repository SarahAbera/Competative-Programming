n = int(input())
graph = []
for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

count = 0
for row in range(n):
    for col in range(n):
        if graph[row][col] == 1:
            count += 1
print(count//2)
