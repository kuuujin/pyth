def knapSack(w, weight, value, n):
    k = [[0 for j in range(w+1)] for i in range(n+1)]
    for i in range(1, n+1):
        curW = weight[i-1]
        curV = value[i-1]
        print(f"물건 {i} 고려 중 (무게: {curW}, 가치: {curV})")
        for j in range(1, w+1): 
            if weight[i-1] > j:
                k[i][j] = k[i-1][j]
                print(f"이전 값 유지: {k[i][j]}")
            else:
                include = value[i-1] + k[i-1][j - weight[i-1]]
                exclude = k[i-1][j] 
                k[i][j] = max(include,exclude)
                decision = "선택함" if k[i][j] == include else "선택 안함"
                print(f"비교: [넣음 {include}] vs [안 넣음 {exclude}] -> 결정: {k[i][j]} ({decision})")
        print(f"아이템 {i} 처리 후 테이블 행: {k[i]}")                         
    return k[n][w]

value = [25, 15, 20, 30]
weight = [3, 1, 2, 4]
C = 7
n = len(value)

print("최대 가치 =", knapSack(C, weight, value, n))