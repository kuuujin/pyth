INF = 9999

def findAllPairShortestPath(graph, n):
    dist = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    print(f"--- 초기 상태 (k = -1) ---")
    printSolution(dist, n)
    print("----------------------------\n")

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        print(f"--- k = {k} (정점 {k} 경유) ---")
        printSolution(dist, n)
        print("----------------------------\n")

def printSolution(dist, n):
    
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print(f"{'INF':>4}", end=" ")
            else:
                print(f"{dist[i][j]:4}", end=" ")
        print("")

graph = [[0, INF, 2, INF],
         [1, 0, INF, INF],
         [INF, 8, 0, 3],
         [6, 4, INF, 0]]
n = 4

findAllPairShortestPath(graph, n)