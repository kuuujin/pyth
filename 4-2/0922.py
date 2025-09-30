def HeapSort(A):
    eh = len(A) - 1
    buildHeap(A, eh)

    while(eh>1):
        A[1], A[eh] = A[eh], A[1]
        eh = eh - 1
        pushDown(A, 1, eh//2, eh)

def buildHeap(A, eh):
    bh = len(A)//2 + 1
    while(bh > 1):
        bh = bh - 1
        x = bh
        pushDown(A, x, bh ,eh)

def pushDown(A,x,bh,eh):
    y=findLarger(A, x, eh)
    while(A[x]<A[y]):
        A[x], A[y] = A[y], A[x]
        x=y
        y=findLarger(A, x, eh)

def findLarger(A, x, eh):
    y = 0
    if (2*x+1<=eh):
        if(A[2*x]>A[x] or A[2*x+1]>A[x]):
            if(A[2*x]>=A[2*x+1]): y = 2*x
            else: y = 2*x+1
    elif(2*x<=eh and A[2*x]>A[x]): y = 2*x
    return y

A = [0,1,2,6,4,8,7]
print(f"정렬 전 배열: {A}")
HeapSort(A)
print(f"정렬 후 배열: {A}")