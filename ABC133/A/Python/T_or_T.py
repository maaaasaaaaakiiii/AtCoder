N, A, B = map(int, input().split())
total = A * N if A * N < B else B
print(total)