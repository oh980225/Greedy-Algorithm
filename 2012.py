import sys

def _2012(N, N_list):
  N_list.sort()
  result = 0
  for i in range(N):
    temp = N_list[i]
    i += 1
    if temp != i:
      result += abs(temp-i)
  return result

N = int(sys.stdin.readline())
N_list = list()

for i in range(N):
  n = int(sys.stdin.readline())
  N_list.append(n)

print(_2012(N, N_list))