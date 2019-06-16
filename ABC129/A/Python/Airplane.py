P, Q, R = map(int, input().split())

times = []
times.append(P+Q)
times.append(P+R)
times.append(Q+R)

print(min(times))