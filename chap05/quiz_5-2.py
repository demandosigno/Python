def is_leapyear(y):
    return (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)) 

year = int(input('西暦を入力してください＞＞'))
if is_leapyear(year):
    print(f'西暦{year}年はうるう年です')
else:
    print(f'西暦{year}年はうるう年ではありません')