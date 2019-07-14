S = input()
s_tmp = S[0]
con = "Good"
for i in range(1, len(S)):
    if s_tmp == S[i]:
        con = "Bad"
    s_tmp = S[i]
print(con)