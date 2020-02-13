# 백준 2217번
N = int(input())
min_rope = 0
max_value = 0
N_list = list()
for i in range(N):
  i = int(input())
  N_list.append(i)

N_list.sort()

while N_list:
  min_rope = N_list[0]
  temp = len(N_list)*min_rope
  N_list.pop(0)
  if temp > max_value:
    max_value = temp

print(max_value)