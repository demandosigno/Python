count = 1
response = 'y'
print('カレーを召し上がれ')
while response == 'y':
    print(f'{count}皿のカレーを食べました')
    response = input('おかわりはいかがですか？（y/n）>>')
    count += 1
print('ごちそうさまでした')