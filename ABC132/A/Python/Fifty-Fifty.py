S = input()
dict_S = {}
for s in S:
    if s not in dict_S:
        dict_S[s] = 1
    else:
        dict_S[s] += 1

if len(dict_S) > 2:
    print("No")
else:
    cnt = 0
    for s in dict_S.values():
        if s == 2:
            cnt += 1
    if cnt == 2:
        print("Yes")
    else:
        print("No")