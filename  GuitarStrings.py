# 백준 1049번
def min_pay(pk, pi, N):
  result = 0
  if pk == 0 or pi == 0:
    return 0
  elif pk >= pi*6:
    result = N*pi
    return result
  else:
    k = pk // pi
    while k < N:
      N -= 6
      result += pk
    if N > 0:
      result += N*pi
    return result

N, M = map(int, input().split())
pk_list = list()
pi_list = list()


for i in range(M):
  pk, pi = map(int, input().split())
  pk_list.append(pk)
  pi_list.append(pi)

pk = min(pk_list)
pi = min(pi_list)

result = min_pay(pk, pi, N)
print(result)