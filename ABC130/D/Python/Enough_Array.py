N, K = map(int, input().split())
a_list = list(map(int, input().split()))

cnt = 0
for index_i in range(N):
    tmp_sum = 0
    for index_j in range(index_i, N):
        tmp_sum += a_list[index_j]
        if tmp_sum >= K:
            cnt += len(a_list[index_j:])
            break
print(cnt)