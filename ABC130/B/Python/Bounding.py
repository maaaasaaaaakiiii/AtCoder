N, X = map(int, input().split())
L_list = list(map(int, input().split()))

cnt = 0
D_i = 0
for L in L_list:
    D_i = D_i + L
    if D_i <= X:
        cnt += 1

print(cnt + 1)