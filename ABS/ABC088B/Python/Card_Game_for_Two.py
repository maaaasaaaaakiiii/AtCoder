N = int(input())
a_list = sorted(map(int, input().split()), reverse=True)
A_count, B_count = 0, 0
for i in range(N):
    if i % 2 == 0:
        A_count += a_list[i]
    else:
        B_count += a_list[i]

print(A_count - B_count)