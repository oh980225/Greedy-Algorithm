# https://has3ong.tistory.com/528 참고했다.
# 백준 1946번
import sys

def f1946():
  T = int(input())
  for i in range(T):
    N = int(input())
    N_list = list()
    result = 0
    for j in range(N):
      a, b = map(int, sys.stdin.readline().split())
      N_list.append((a,b)) 

    N_list.sort(key= lambda num:num[0])
    temp = 100001
    for num in N_list:
      if temp > num[1]:
        result += 1
        temp = num[1]
    print(result)
f1946()