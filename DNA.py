def _1969(N, M, str_list, checked):
  str_result = ""
  num_result = 0
  for i in range(M):
    for string in str_list:
      if string[i] == 'A':
        checked[0] += 1
      elif string[i] == 'C':
        checked[1] += 1
      elif string[i] == 'G':
        checked[2] += 1
      elif string[i] == 'T':
        checked[3] += 1
    max_value = max(checked)
    idx = checked.index(max_value)
    if idx == 0:
      str_result += "A"
    elif idx == 1:
      str_result += "C"
    elif idx == 2:
      str_result += "G"
    elif idx == 3:
      str_result += "T"
    num_result += (sum(checked) - max_value)
    checked = [0, 0, 0, 0]
  print(str_result)
  print(num_result)


N, M = map(int, input().split())
str_list = list()
checked = [0, 0, 0, 0]

for i in range(N):
  value = input()
  str_list.append(value)

_1969(N, M, str_list, checked)