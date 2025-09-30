set = [1,1,2,2,2,8]
found_pieces = list(map(int,input("").split()))
result = [cor - found for cor, found in zip(set,found_pieces)]
print(*result)