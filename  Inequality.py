# https://rebas.kr/755 참고했다.
# 백준 2529번
def possible(i, j, k):
  if k == '<':
    return i < j
  else:
    return i > j

def solve(cnt, s, c, n, op):
  global mx, mn
  if cnt == n+1:
    if 0 == len(mn):
      mn = s
    else:
      mx = s
    return 
  for i in range(10):
    if not c[i]:
      if cnt == 0 or possible(s[-1], str(i), op[cnt-1]):
        c[i] = True
        solve(cnt+1, s+str(i), c, n, op)
        c[i] = False

k = int(input())
k_list = list(input().split())
num_list = [False for i in range(10)]
mx, mn ="", ""
result = solve(0, "", num_list, k, k_list)
print(mx)
print(mn)