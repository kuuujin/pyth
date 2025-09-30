A = [10,12,13,14,18,20,25,27,30,35,40,45,47]

def BinarySearch(A,first,last,x):
    if first > last: return -1
    else:
        mid = ((first+last)//2)
        if x == A[mid]: return mid
        elif x < A[mid]: return BinarySearch(A,first,mid -1,x)
        else: return BinarySearch(A,mid+1,last,x)

print(BinarySearch(A,0,12,18))