N, A, B = map(int, input().split())
all_sum = 0
for i in range(1, N+1):
    tmp_sum = 0
    for char_i in str(i):
        tmp_sum += int(char_i)
    if A <= tmp_sum <= B:
        all_sum += i
print(all_sum)
