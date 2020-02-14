# 백준 1541번
ex = list(input())
num = ""
num_list = list()
toggle = False
result = 0

for idx, i in enumerate(ex):
  if idx == len(ex)-1:
    num += i
    num_list.append(int(num))
    num = ""
    break
  if i != '-' and i != '+':
    num += i
  else:
    num_list.append(int(num))
    num = ""
    num_list.append(i)

for idx, num in enumerate(num_list):
  if num == '-':
    toggle = True
  if num == '-' or num == '+':
    num = 0
  if toggle:
    result -= num
  else:
    result += num

print(result)