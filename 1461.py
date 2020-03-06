def _1461(N, M):
  books = list(map(int, input().split()))
  plus_position = list()
  minus_position = list()
  result_list = list()
  result = 0

  for book in books:
    if book < 0:
      minus_position.append(book)
    else:
      plus_position.append(book)
  
  plus_position.sort(reverse=True)
  minus_position.sort()

  temp = M
  for position in plus_position:
    if temp == M:
      result_list.append(abs(position))
      temp = 1
    else:
      temp += 1

  temp = M  
  for position in minus_position:
    if temp == M:
      result_list.append(abs(position))
      temp = 1
    else:
      temp += 1
  
  result_list.sort()
  result += result_list.pop()
  
  for element in result_list:
    result += element*2
  
  return result
  
  


N, M = map(int, input().split())

print(_1461(N, M))