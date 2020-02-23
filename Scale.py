# 백준 2437번
# https://jaimemin.tistory.com/756 참고했다.
def _2437(N_list):
  if N_list[0] != 1:
    return 1
  else:
    result = 1
    for i in range(len(N_list)-1):
      i += 1
      if N_list[i] <= result+1:
        result += N_list[i]
      else:
        result += 1
        return result
    return result+1

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()
result = _2437(N_list)
print(result)