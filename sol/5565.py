tot = int(input())
books = []
for _ in range (9):
    a = int(input())
    books.append(a)
print(tot - sum(books))