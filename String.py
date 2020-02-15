# 백준 1120번
def difference(a,b):
  result = 0
  for idx, i in enumerate(a):
    if i != b[idx]:
      result += 1
  return result

A, B = input().split()
new_list = list()
res_list = list()

for i in range(len(B)-len(A)+1):
  temp = B[i:i+len(A)]
  new_list.append(temp)

for i in new_list:
  res_list.append(difference(A, i))

result = min(res_list)
print(result)