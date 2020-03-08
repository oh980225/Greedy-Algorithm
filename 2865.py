def _2865(N, M, K):
  score = list()
  total_list = list()
  K_list = list()
  result = 0

  for i in range(M):
    temp_list = list(map(float, input().split()))
    score.extend(temp_list)
  
  toggle = False
  pair = [0, 0]

  for idx, element in enumerate(score):
    if toggle:
      toggle = False
      pair[1] = element
      total_list.append(pair)
      pair = [0 ,0]
    else:
      toggle = True
      pair[0] = element

  total_list.sort(key = lambda x:x[1], reverse=True)

  for element in total_list:
    if (K_list.count(element[0]) == 0) and (len(K_list) < K):
      K_list.append(element[0])
      result += element[1]

  return result

N, M, K = map(int, input().split())

result = round(_2865(N, M, K), 1)
print(result)