# 백준 11047번
N, K = map(int, input().split())
N_list = list()
result = 0
temp = 0

for i in range(N):
  num = int(input())
  N_list.append(num)
N_list.reverse()

while K != 0:
  if (K-N_list[0]) < 0:
    N_list.pop(0)
  else:
    temp = K // N_list[0]
    result += temp
    K = K - temp*N_list[0]
    N_list.pop(0)

print(result)