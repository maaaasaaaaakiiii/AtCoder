N = int(input())
list_p = list(map(int, input().split()))
cnt = 0
for i in range(1, N-1):
    if list_p[i-1] < list_p[i] < list_p[i+1] or list_p[i+1] < list_p[i] < list_p[i-1]:
        cnt += 1
print(cnt)