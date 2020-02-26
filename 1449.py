def _1449(N, L, position):
  position.sort()
  start = position[0] - 0.5
  end = start + L
  result = 1
  position = position[1:]
  for p in position:
    if p+0.5 <= end and p-0.5 >= start:
      continue
    else:
      start = p - 0.5
      end = start + L
      result += 1
  return result

N, L = map(int, input().split())
position = list(map(int, input().split()))

print(_1449(N, L, position))