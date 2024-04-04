print('identityの変化を比較')

names = list() # リストの場合
print(f'list（変更前）: {id(names)}')
names.append('松田')
print(f'list（変更後）: {id(names)}')

name = '松田'   # 文字列の場合
print(f'str（変更前） : {id(name)}')
name = 'スーパー' + name
print(f'str（変更後） : {id(name)}')