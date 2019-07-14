N = int(input())
list_d = list(map(int, input().split()))
list_d = sorted(list_d)
print(list_d[len(list_d)//2] - list_d[len(list_d)//2 - 1])