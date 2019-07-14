N, L = map(int, input().split())
L_list = [n+L for n in range(N)]
if 0 in L_list:
    L_list.remove(0)
    print(sum(L_list))
elif L_list[0] > 0:
    print(sum(L_list[1:]))
else:
    print(sum(L_list[:-1]))