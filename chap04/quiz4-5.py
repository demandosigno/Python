temp = list()
for n in range(3):
    data = float(input(f'{n+1}個目のデータを入力>>'))
    temp.append(data)

for o in temp:
    print(o)

temp_new = list()
for count in range(len(temp)):
    if count == 2:
        temp_new.append('N/A')
    else:
        temp_new.append(temp[count])
print(temp)
print(temp_new)

total = 0
for data in temp_new:
    if isinstance(data, float):
        total = total + data
print(total / (len(temp_new) - 1))