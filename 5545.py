N = int(input()) 
dow_price, toping_price = map(int, input().split())
dow_cal = int(input())
total_toping_cal = 0
toping_cal_list = list()
max_cal = dow_cal
best_cal = max_cal // dow_price

for i in range(N):
  toping_cal = int(input())
  toping_cal_list.append(toping_cal)

toping_cal_list.sort(reverse=True)

for i in range(N):
  toping_cal = toping_cal_list[i]
  temp_cal = max_cal + toping_cal
  if best_cal > (temp_cal // (dow_price + toping_price*(i+1))):
    break
  best_cal = (temp_cal // (dow_price + toping_price*(i+1)))
  max_cal = temp_cal

result = best_cal
print(result)