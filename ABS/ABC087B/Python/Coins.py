A = int(input())
B = int(input())
C = int(input())
X = int(input())
cnt = 0
for A_500 in range(A+1):
    for B_100 in range(B+1):
        for C_50 in range(C+1):
            if (A_500 * 500) + (B_100 * 100) + (C_50 * 50) == X:
                cnt += 1
print(cnt)