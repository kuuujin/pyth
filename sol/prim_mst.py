INF = 9999
def prim_mst(w,n):
    near = [0 for _ in range(n)]
    is_blue = [False for _ in range(n)]
    print("최소 비용 신장 트리에 포함된 간선 목록")
    print("\t간선\t가중치")
    is_blue[1:] = [True] * (n - 1)
    near[1:] = [0 for _ in range(n - 1)]
    for _ in range(1, n):
        minval  = INF
        new_red = -1
        for b in range(n):
            if is_blue[b]: 
                if w[b][near[b]] < minval:
                    minval = w[b][near[b]]
                    new_red = b
        is_blue[new_red] = False
    
        print(f"\t{near[new_red]} - {new_red}\t {w[new_red][near[new_red]]}")

        for b in range(n):
            if is_blue[b] and w[b][new_red] < w[b][near[b]]:
                near[b] = new_red

graph = [[0,2,INF,INF,4],[2,0,8,INF,4],[INF,8,0,7,6],[INF,INF,7,0,3],[4,4,6,3,0]]
prim_mst(graph,5)