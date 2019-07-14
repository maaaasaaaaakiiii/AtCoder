N = int(input())
A_list = list(map(int, input().split()))
cnt = 0
tmp = False
while True:
    for i in range(len(A_list)):
        if A_list[i] % 2 == 0:
            A_list[i] = int(A_list[i]/2)
        else:
            tmp = True
            break
    if tmp:
        break
    else:
        cnt += 1
print(cnt)
