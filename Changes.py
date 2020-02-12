# 백준 5585번
N_list = [500, 100, 50, 10, 5, 1]
price = 1000
result = 0

pay = int(input())
changes = price - pay

for N in N_list:
  if changes-N >= 0:
    temp = changes // N
    changes -= N*temp
    result += temp

print(result)