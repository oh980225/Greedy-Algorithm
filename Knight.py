# 백준 1783번
# https://yhk-0811.tistory.com/33 참고했다.
def _1783(x, y, N, M):
  if N == 1:
    return 1
  elif N == 2:
    return min(4, int((M+1)/2))
  else:
    if M < 7:
      return min(4, M)
    elif M == 7:
      return 5
    else:
      return M-2

N, M = map(int, input().split())
result = _1783(1, 1, N, M)
print(result)