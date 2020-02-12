# 백준 1931번
# https://daimhada.tistory.com/38 참고했음.
N = int(input())
N_list = [[0, 0] for i in range(N)]
start = 0
result = 0

# time[0]는 start_time, time[1]는 end_time
for time in N_list:
  time[0], time[1] = map(int, input().split())

# end_time이 작은 요소부터 정렬하되, 같을 경우 start_time이 작은 요소가 먼저 정렬되게 한다.
N_list.sort(key=lambda time:time[0])
N_list.sort(key=lambda time:time[1])

for time in N_list:
  if time[0] >= start:
    result += 1
    start = time[1]
  
print(result)