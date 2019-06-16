N = int(input())
W_list = list(map(int, input().split()))

min_abs = -1
for n in range(N):
    S1 = W_list[:n+1]
    S2 = W_list[n+1:]
    tmp_abs = abs(sum(S1) - sum(S2))
    if min_abs == -1:
        min_abs = tmp_abs
    elif min_abs > tmp_abs:
        min_abs = tmp_abs

print(min_abs)
