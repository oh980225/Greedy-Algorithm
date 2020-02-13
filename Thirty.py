# 백준 10610번
def thirty(n):
  num_list = list(map(int, n))
  if not 0 in num_list:
    return -1
  if sum(num_list)%3 != 0:
    return -1
  num_list.sort(reverse=True)
  result = ""
  for num in num_list:
    result += str(num)
  return result

N = input()
print(thirty(N))