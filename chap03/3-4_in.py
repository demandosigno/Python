name = input('あなたの名前を教えてください >>')
print(f'{name}さん、こんにちは')
food = input(f'{name}さんの好きな食べ物を教えてください >>')
if 'カレー' in food:
    print('素敵です。カレーは最高ですよね!!')
else:
    print(f'私も{food}が好きですよ')