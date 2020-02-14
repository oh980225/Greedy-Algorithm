# 백준 2875번
# https://has3ong.tistory.com/463 참고했다.
N, M, K = map(int, input().split())
result = 0

while K > 0:
  if N//2 < M:
    M -= 1
  else:
    N -= 1
  K -= 1

if N//2 >= M:
  result = M
else:
  result = N//2

print(result)