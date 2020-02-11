# 백준 11399번
N = int(input())
p_list = list(map(int, input().split()))

result_list = sorted(p_list)
sum = [0, 0]

for i in result_list:
  sum[0] += i
  sum[1] += sum[0]

print(sum[1])