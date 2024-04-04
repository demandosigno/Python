x = ['ABC']
print(f'id(x[0]) = {id(x[0])}')
print(f'id(x)    = {id(x)}')
# y = [input('文字を入力してください：')]
y = ['ABC']
print(f'id(y[0]) = {id(y[0])}')
print(f'id(y)    = {id(y)}')
print(x[0] == y[0])
print(id(x[0]) == id(y[0]))
print(id(x) == id(y))
y = x
print(f'id(x)    = {id(x)}')
print(f'id(y)    = {id(y)}')
y[0] = 'XYZ'
print(f'id(x)    = {id(x)}')
print(f'id(y)    = {id(y)}')
print(f'id(x[0]) = {id(x[0])}')
print(f'id(y[0]) = {id(y[0])}')
print(x[0])
a = 1
b = 2
b = 7
list1 = [1,2]
list2 = [1,7]
print(id(list1))
print(id(list2))
print(id(list1[0]))
print(id(list2[1]))
print(id(a))
print(id(b))