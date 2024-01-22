count = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 'Lift off!']
for now in count:
    print(now, end='')
    print('、')

for num in range(11):
    print(count[num], end='')
    print('、')

for num2 in range(10):
    print(f'{10 - num2}、', end='')
print('Lift off!')