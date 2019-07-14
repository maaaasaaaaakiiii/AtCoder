W, H, x, y = map(int, input().split())
area = float(W) * float(H) / 2
way = 1 if W / 2 == x and H / 2 == y else 0
print(area, way)