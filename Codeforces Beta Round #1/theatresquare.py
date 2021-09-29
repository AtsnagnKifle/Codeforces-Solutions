import math

n, m, a = map(int, input().split())

ans = math.ceil(n/a) * math.ceil(m/a)
print(ans)
